def PickupMinutes(userX :int, userY :int, d1X :int, d1Y :int, d2X :int, d2Y :int, d3X :int, d3Y :int) -> int:
    d1 = abs(userX-d1X) + abs(userY-d1Y)
    d2 = abs(userX-d2X) + abs(userY-d2Y)
    d3 = abs(userX-d3X) + abs(userY-d3Y)
    return min(d1, d2, d3) * 2

userX, userY, d1X, d1Y, d2X, d2Y, d3X, d3Y = [int(input()) for i in range(8)]
print(PickupMinutes(userX, userY, d1X, d1Y, d2X, d2Y, d3X, d3Y))