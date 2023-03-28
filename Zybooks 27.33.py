frames = [0] * 9
throws = [int(input()) for i in range(21)]
j = 2
prevFrame = 0
for i in range(9):
    if throws[j-2] == 10:
        frames[i] = prevFrame + 10 + throws[j-1] + throws[j]
        j += 1
    elif throws[j-2] + throws[j-1] == 10:
        frames[i] = prevFrame + 10 + throws[j-1]
        j += 2
    else:
        frames[i] = throws[j-2] + throws[j-1]
        j += 2
    prevFrame = frames[i]
print(" ".join([str(throw) for throw in frames]), end="")
if throws[j-2] + throws[j-1] >= 10:
    print("", prevFrame + sum(throws[j-2:j+1]))

