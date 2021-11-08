



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
    # Check for any paired or suited cards
    for this_card in all_cards:
        hits = 1
        suit_hits = 1
        print("This Card: rank = ", this_card["rank"], ", suit = ", this_card["suit"])
        consider = False
        for check_card in all_cards:
            if consider == True:
                print ("Comparing against: rank = ", check_card["rank"], ", suit = ", check_card["suit"])
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
            # 3 of a kind
            score += 1
        if suit_hits == 5:
            # flush
            score += 5
    
    # Return the score for this hand
    return score
