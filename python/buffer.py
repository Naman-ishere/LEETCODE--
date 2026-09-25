def canSellCookies(bills):
    price = 5
    galla = 0
    for cash in bills:
        if cash == price:
            galla += cash
        else:
            galla += cash
            change = cash - price
            if galla >= change:
                galla - change
                return False
            else:
                return False

bills = [5, 5, 5, 10, 20, 10, 10, 10]
print(canSellCookies(bills))
