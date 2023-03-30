def DigitsToNumber(digits: list[int]) -> int:
    number = 0
    for i in range(len(digits)):
        number += digits[i] * 10 ** i
    return number
digits = [int(input()) for i in range(int(input("Enter length of list ")))]
print(DigitsToNumber(digits))