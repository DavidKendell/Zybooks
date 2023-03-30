def GetAge(birthMonth: int, birthDay: int, birthYear: int, currMonth: int, currDay: int, currYear: int) -> int:
    diffY = currYear - birthYear
    diffM = currMonth - birthMonth
    diffD = currDay - birthDay
    if diffY < 1:
        return 0
    age = diffY
    if diffM < 0 or diffM == 0 and diffD < 0:
        return age - 1
    return age

birthMonth, birthDay, birthYear, currMonth, currDay, currYear = [int(input()) for i in range(6)]
print(GetAge(birthMonth, birthDay, birthYear, currMonth, currDay, currYear))