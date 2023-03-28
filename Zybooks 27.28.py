n = int(input())
nums = [int(input()) for i in range(n)]
prev = 0
if len(nums) > 0:
    prev = nums[0]
for num in nums:
    if num > prev:
        print("Unsorted")
        break
    prev = num
else:
    print("Sorted")