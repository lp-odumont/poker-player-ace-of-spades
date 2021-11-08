
from card_utils import convert_card_to_int
from evaluate_hand import analyze_hand
from evaluate_hole import get_hand_strength



class Player:
    VERSION = "v0.3"


    def betRequest(self, game_state):
        print("round = ", game_state["round"])
        print("bet_index = ", game_state["bet_index"])
        hand_strength = get_hand_strength(game_state)

        is_raised = game_state["current_buy_in"] > game_state["small_blind"]
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
            if (hand_strength < 10):
                # Raise (unless already raised)
                if is_raised:
                    # Raise (3 x Big Blind)
                    return game_state["small_blind"] * 6;
                else:
                    # Call
                    return game_state["current_buy_in"]
            if (hand_strength < 30):
                # Call (unless big raise)
                if (is_raised):
                    # Fold
                    return 0
                else:
                    # Call
                    return game_state["current_buy_in"]
            else:
                # Fold
                return 0
            return 0
        else:
            #simple_strength = analyze_hand(game_state)
            simple_strength = score
            if simple_strength == 0:
                return 0
            elif simple_strength == 1:
                # Call
                return game_state["current_buy_in"]
            elif simple_strength > 1:
                # Raise
                return game_state["current_buy_in"] * simple_strength
        return 0

    def showdown(self, game_state):
        score,potential = analyze_hand(game_state)
        simple_strength = score
        if simple_strength == 0:
            return 0
        elif simple_strength == 1:
            # Call
            return game_state["current_buy_in"]
        elif simple_strength > 1:
            # Raise
            return game_state["current_buy_in"] * simple_strength

