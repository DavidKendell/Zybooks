values = [int(input()) for i in range(12)]
for i in range(0, 9, 4):
    print(" ".join([str(j) for j in values[i:i+4]]))