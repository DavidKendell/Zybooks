date = input()
date = [int(t) for t in date.split(" ")]
date[1] += 1
longmonths = date[1] > 31
shortmonths = date[1] > 30 and date[0] % 2 == 0 and date[0] < 8 or date[0] % 2 == 1 and date[0] >= 8
feb = date[0] == 2 and date[1] > 28
if longmonths or shortmonths or feb:
    date[0] += 1
    date[1] = 1
if date[0] > 12:
    date[0] = 1
    date[1] = 1
    date[2] += 1
print(" ".join([str(i) for i in date]))
