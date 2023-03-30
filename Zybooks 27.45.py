def DigitToWord(digitIn: int) -> str:
    words = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    if digitIn < 0 or digitIn > 9:
        return "Error"
    else:
        return words[digitIn]
def TensDigitToWord(digitIn: int) -> str:
    words = ["twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if digitIn < 2 or digitIn > 9:
        return "Error"
    else:
        return words[digitIn-2]
def TwoDigitNumToWords(digitIn: int) -> str:
    return TensDigitToWord(digitIn//10) + " " + DigitToWord(digitIn%10)

digitIn = int(input())
print(TwoDigitNumToWords(digitIn))