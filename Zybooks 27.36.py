chptList = [int(input()) for i in range(15)]
lower = 0
upper = -1
for i in range(15):
    if not chptList[lower]:
        lower = i
    if chptList[i]:
        upper = i
        continue
    if upper - lower <= 1:
        for j in range(lower, upper+1):
            print(j+1, end=" ") 
    else:
        print(lower+1, "-", upper+1, end=" ", sep="")
    lower = i
else:
    if upper - lower <= 1:
        for j in range(lower, upper+1):
            print(j+1, end=" ") 
    else:
        print(lower+1, "-", upper+1, end=" ", sep="")
if upper == -1:
    print("None")
else:
    print()    
