inches = int(input())
feet, inches = inches // 12, inches % 12
print(feet, "'", inches, '"', sep="")