listInts = [int(input()) for i in range(6)]
listNegInts = [i for i in listInts if i < 0]
print(len(listNegInts))
for i in listNegInts:
    print(i)