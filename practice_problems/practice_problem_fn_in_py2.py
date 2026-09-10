def milkPurchase(almond, oat, soy):
    '''
    milkPurchase determines the type of milk to buy based on how much cents per 100 mL of each milk

    almond - An integer that states how many cents per 100mL for almond milk
    oat - An integer that states how many cents per 100mL for oat milk
    soy - An integer that states how many cents per 100mL for soy milk
    returns - A string of either "Almond", "Oat", "Soy", or "Nothing"

    Examples:
    milkPurchase(40,40,21) -> "Almond"
    milkPurchase(40,25,19) -> "Soy"
    milkPurchase(47,30,29) -> "Oat"
    '''
    if almond < 20:
        return "Almond"
    elif oat < 20:
        return "Oat"
    elif soy < 20:
        return "Soy"

    if almond < 45:
        return "Almond"
    elif oat < 40:
        return "Oat"
    elif soy < 37:
        return "Soy"
    else:
        return "Nothing"

print(milkPurchase(47,30,29))