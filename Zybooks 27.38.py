listSize = int(input())
listNums = [int(input()) for i in range(listSize)]
for i in range(listSize//2):
    temp = listNums[i]
    listNums[i] = listNums[-i-1]
    listNums[-i-1] = temp
for i in listNums:
    print(i, end=" ")
print()