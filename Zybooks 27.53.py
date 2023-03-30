def findNextSubstr(string: str, start: int, substr: str) -> int:
    start = max(start, 0)
    while len(string) - start >= len(substr):
        for i in range(len(substr)):
            if string[i + start] != substr[i]:
                start += 1
                break
        else:
            return start
    return -1

print(findNextSubstr("tastychickentastychicken", -7, "chicken"))