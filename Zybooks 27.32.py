binaryNumber = [int(input()) for i in range(8)]
summed = 0
for i in range(8):
    summed += binaryNumber[7-i] * 2 ** i
print(summed)