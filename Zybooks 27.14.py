n = max(0, int(input("Enter an integer: ")))
n = n // 2 * 2
print("Sequence: " + " ".join([str(i) for i in range(n, -1, -2)]))