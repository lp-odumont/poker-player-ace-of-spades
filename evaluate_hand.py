



from card_utils import convert_card_to_int

def get_all_cards(game_state):
    id = game_state["in_action"]
    data = game_state["players"][id]
    all_cards = data["hole_cards"]
    all_cards += game_state["community_cards"]
    for card in all_cards:
        card["rank"] = convert_card_to_int(card["rank"])
    return all_cards

def analyze_hand(game_state):
    all_cards = get_all_cards(game_state)
    print("All Cards: ", all_cards)
    score = 0
    potential = 0
    cards_left = 7 - len(all_cards)
    # Check for any paired or suited cards
    for this_card in all_cards:
        hits = 1
        suit_hits = 1
        #print("This Card: rank = ", this_card["rank"], ", suit = ", this_card["suit"])
        consider = False
        for check_card in all_cards:
            if consider == True:
                #print ("Comparing against: rank = ", check_card["rank"], ", suit = ", check_card["suit"])
                if (this_card["rank"] == check_card["rank"]):
                    hits += 1
                if (this_card["suit"] == check_card["suit"]):
                    suit_hits += 1

            # Ignore cards up to and including this card
            if (this_card["rank"] == check_card["rank"]) and (this_card["suit"] == check_card["suit"]):
                consider = True;

        if hits == 4:
            # 4 of a kind
            score += 10
        if hits == 3:
            # 3 of a kind
            score += 3
        if hits == 2:
            # pair
            score += 1
            # If top pair, add a point
            is_top_pair = True
            for check_card in all_cards:
                if  check_card["rank"] > this_card["rank"]:
                    is_top_pair = False
            if is_top_pair:
                print ("We have top pair!!")
                score += 1;
        if suit_hits == 5:
            # flush
            score += 5
        if suit_hits == 4 and score < 5:
            if cards_left == 2:
                print ("2 cards for a flush")
                potential += 10
            if cards_left == 1:
                print ("1 card for a flush")
                potential += 5
    
    # Return the score & potential for this hand
    return score,potential
