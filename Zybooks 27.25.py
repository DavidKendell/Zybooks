threshold = float(input())
for i in range(30, 41):
    GPA = i / 10
    score = 16*threshold - 2.5/4*1600*GPA
    print(GPA, score)