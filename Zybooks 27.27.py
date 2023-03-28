n = int(input())
nums = [int(input()) for i in range(n)]
diffs = [abs(nums[i+1] - nums[i]) for i in range(n-1)]
print(max(diffs))