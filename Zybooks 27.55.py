def rotateThreeValues(x: int, y: int, z: int) -> tuple[int, int, int]:
    return z, x, y

x, y, z = [int(input()) for i in range(3)]
x, y, z = rotateThreeValues(x, y, z)
print(x, y, z)