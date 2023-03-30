numItems = int(input())
listItems = [input() for i in range(numItems)]
currSequence = 0
longestSequence = 0
for item in listItems:
    if item == "I":
        longestSequence = max(longestSequence, currSequence)
        currSequence = 0
    else:
        currSequence += 1

print(longestSequence)