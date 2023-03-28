from math import sqrt

diagonal = float(input())
for width in range(1, int(diagonal) + 1):
    height = sqrt(diagonal**2 - width**2)
    print(float(width), height)