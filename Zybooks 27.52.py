def FindNextCharInString(inputString: str, startIndex: int, searchChar: str) -> int:
    if startIndex >= len(inputString):
        return -1
    for i in range(startIndex, len(inputString)):
        if inputString[i] == searchChar:
            return i
    return -1
inputString, startIndex, searchChar = input(), int(input()), input()
print(FindNextCharInString(inputString, startIndex, searchChar))
