from card_utils import convert_card_to_int

import logging
logging.getLogger().setLevel(logging.DEBUG)

def get_hand_strength(game_state):
    print("Caclulate")
    id = game_state["in_action"]
    data = game_state["players"][id]
    print("id=%i data=%s "%(id,data))
    hole = data["hole_cards"]
    hole_0 = hole[0]
    hole_1 = hole[1]
    is_suit = hole_0["suit"] == hole_1["suit"]
    h_0 = convert_card_to_int(hole_0["rank"])
    h_1 = convert_card_to_int(hole_1["rank"])
    is_pair = h_0 == h_1
    
    if h_0 < h_1:
        temp = h_1
        h_1 = h_0
        h_0 = temp

    score = 0
    if is_pair:
        score = (14-h_0) * 1.5
    else:
        score += (14-h_0) * 3
        distance = h_0 - h_1
        score += distance * 3


    print("hole 0 %s"%hole_0)
    print("hole 1 %s"%hole_1)
    print("score %d"%score)
    logging.info("Calculated Hole Score: %s", score)

    return score
