def maxFive(a: int, b: int, c: int, d: int, e: int) -> int:
    maxInt = a
    if b > maxInt:
        maxInt = b
    if c > maxInt:
        maxInt = c
    if d > maxInt:
        maxInt = d
    if e > maxInt:
        maxInt = e
    return maxInt
a, b, c, d, e = [int(input()) for i in range(5)]
print(maxFive(a, b, c, d, e))