#Can't pass by reference but python allows multiple return values
def Ascend3(x: int, y: int, z: int) -> tuple[int]:
    if x > y:
        temp = x
        x = y
        y = temp
    if y > z:
        temp = y
        y = z
        z = temp
    if x > y:
        temp = x
        x = y
        y = temp
    return x, y, z
a, b, c = [int(input()) for i in range(3)]
a, b, c = Ascend3(a, b, c)
print(a, b, c)
    