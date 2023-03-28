print("Enter an integer")
num = abs(int(input()))
print("Sequence: ", end="")
print(" ".join([str(i) for i in range(-num, num+1)]))