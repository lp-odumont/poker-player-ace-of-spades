def get_hand_strength(game_state):
    print("Caclulate")
    id = game_state["in_action"]
    data = game_state["players"][id]
    print("id=%i data=%s "%(id,data))
    hole = data["hole_cards"]
    hole_0 = hole[0]
    hole_1 = hole[1]
    is_same = hole_0["suit"] == hole_1["suit"]
    h_0 = hole_0["rank"]
    h_1 = hole_0["rank"]

    print(" %s"%hole_0)
    print(hole_1)

    return 18
