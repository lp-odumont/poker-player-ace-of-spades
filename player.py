
from card_utils import convert_card_to_int
from evaluate_hand import analyze_hand
from evaluate_hole import get_hand_strength



class Player:
    VERSION = "v0.7"


    def betRequest(self, game_state):
        print("round = ", game_state["round"])
        print("bet_index = ", game_state["bet_index"])
        hand_strength = get_hand_strength(game_state)

        is_raised = game_state["current_buy_in"] > (game_state["small_blind"] * 2)
        is_big_raise = game_state["current_buy_in"] > (game_state["small_blind"] * 10)
        print("small_blind = ", game_state["small_blind"])
        print("current_buy_in = ", game_state["current_buy_in"])
        print("is_raised = ", is_raised)

        num_community_cards = len(game_state["community_cards"])
        print("num_community_cards = ", num_community_cards)
        
        # For testing only
        score,potential = analyze_hand(game_state)
        print ("Test score = ",score, ", potential = ", potential)

        if num_community_cards == 0:
            # Pre-flop
            print("Pre flop hand strength: ", hand_strength)
            if (hand_strength < 10):
                # Great hand!
                # Always raise 3 * min raise
                bet_amount = game_state["current_buy_in"] + (game_state["minimum_raise"] * 2)
                print ("Great Hand, will bet ", bet_amount)
                return bet_amount
                # Raise (unless already raised)
                #if is_raised:
                #    # Raise (3 x Big Blind)
                #    return game_state["small_blind"] * 6;
                #else:
                #    # Call
                #    return game_state["current_buy_in"]
            if (hand_strength < 25):
                # Good hand
                # Call (unless big raise)
                if is_raised:
                    if is_big_raise:
                        # Fold
                        print ("Good hand, fold due to raise")
                        return 0
                    else:
                        # Call
                        bet_amount = game_state["current_buy_in"]
                        print ("Good hand, call small raise ", )
                        return bet_amount
                else:
                    # Call
                    bet_amount = game_state["current_buy_in"]
                    print ("Good hand, call ", )
                    return bet_amount
            else:
                # Fold
                print ("Fold pre-flop")
                return 0
            return 0
        else:
            # Post-flop
            simple_strength = score
            print("Post flop: Score = ", score, "Potential = ", potential)
            if simple_strength == 0:
                if potential == 0:
                    print ("Fold post-flop (missed)")
                    return 0
                else:
                    # Call
                    bet_amount = game_state["current_buy_in"]
                    print ("Call post-flop due to potential: ", bet_amount)
                    return bet_amount
            elif simple_strength == 1:
                # Call
                bet_amount = game_state["current_buy_in"]
                print ("Call post-flop due to small pair: ", bet_amount)
                return bet_amount
            elif simple_strength > 1:
                # Raise
                bet_amount = game_state["current_buy_in"] + (game_state["minimum_raise"] * (simple_strength - 1))
                print ("Raise post-flop: ", bet_amount)
                return bet_amount
        return 0

    def showdown(self, game_state):
        pass

