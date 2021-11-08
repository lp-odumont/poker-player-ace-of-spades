
def convert_card_to_int(card_value):
    if card_value == "J":
        return 11
    elif card_value == "Q":
        return 12
    elif card_value == "K":
        return 13
    elif card_value == "A":
        return 14
    else:
        return int(card_value)

