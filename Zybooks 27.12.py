alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numberplate = list(input())
numberplate = [int(i) if i not in alphabet else i for i in numberplate]
carry = (numberplate[5] + 1) // 10
numberplate[5] = (numberplate[5] + 1) % 10
for i in range(4, 2, -1):
    nextnum = numberplate[i] + carry
    carry = (nextnum) // 10
    numberplate[i] = (nextnum) % 10
for i in range(2, -1, -1):
    nextchar = alphabet.index(numberplate[i])+carry
    numberplate[i] = alphabet[nextchar % 26]
    carry = nextchar // 26
print("".join([str(i) for i in numberplate]))