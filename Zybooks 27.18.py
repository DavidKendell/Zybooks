n = int(input())
print(n % 10)
n //= 10
while n > 0:
    print(n % 10)
    n //= 10