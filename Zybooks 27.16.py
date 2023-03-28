nums = []
x = int(input())
while x != 0:
    nums.append(x)
    x = int(input())
valid = [i for i in nums if i in range(2, 13)]
average = 0
if len(nums) == 0:
    print(0)
else:
    if len(valid) > 0:
        average = sum(valid) / len(valid)
print(f"Average: {average}")
print(f"Valid: {len(valid)}")
print(f"Invalid: {len(nums) - len(valid)}")