#Python doesn't have pass by reference so using return multiple values instead
def CentsToDollarsCents(inputCents) -> tuple[int, int]:
    dollars = inputCents // 100
    cents = inputCents % 100
    return dollars, cents

dollars, cents = CentsToDollarsCents(int(input()))
print(dollars, "dollars", cents, "cents")