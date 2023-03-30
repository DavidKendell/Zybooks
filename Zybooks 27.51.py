def NumToStringWithCommas(num: int) -> str:
    numstr = str(num)
    offset = len(numstr) - 3 - ((len(numstr)-1)//3)*3
    return ",".join([numstr[max(0, i+offset):i+offset+3] for i in range(0, len(numstr), 3)])

userNum = int(input())
print(NumToStringWithCommas(userNum))