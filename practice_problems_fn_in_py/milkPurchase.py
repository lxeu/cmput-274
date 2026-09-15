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
    GLOBALLIMIT = 20
    ALMONDLIMIT = 45
    OATLIMIT = 40
    SOYLIMIT = 37
    
    if almond < GLOBALLIMIT:
        return "Almond"
    if oat < GLOBALLIMIT:
        return "Oat"
    if soy < GLOBALLIMIT:
        return "Soy"

    if almond < ALMONDLIMIT:
        return "Almond"
    if oat < OATLIMIT:
        return "Oat"
    if soy < SOYLIMIT:
        return "Soy"
    else:
        return "Nothing"

print(milkPurchase(47,30,29))