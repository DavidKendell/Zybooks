def main() -> int:
    userValues = [int(input()) for i in range(10)]
    counts = [0 for i in range(100)]
    for i in userValues:
        if i < 0 or i > 99:
            print("Invalid input:", i, "is not in 0-99")
            return 1
        counts[i] += 1
    print(counts.index(max(counts)), max(counts))
    return 0
main()