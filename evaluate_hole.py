from card_utils import convert_card_to_int

def get_hand_strength(game_state):
    print("Caclulate")
    id = game_state["in_action"]
    data = game_state["players"][id]
    print("id=%i data=%s "%(id,data))
    hole = data["hole_cards"]
    hole_0 = hole[0]
    hole_1 = hole[1]
    is_same = hole_0["suit"] == hole_1["suit"]
    h_0 = convert_card_to_int(hole_0["rank"])
    h_1 = convert_card_to_int(hole_1["rank"])
    
    score = 0
    if not is_same:
        score += 10
    if h_0 < h_1:
        temp = h_1
        h_1 = h_0
        h_0 = temp

    if h_0 != h_1:
        score +=10
    
    score += 15-h_0
    

    print("hole 0 %s"%hole_0)
    print("hole 1 %s"%hole_1)
    print("score %d"%score)

    return 18
