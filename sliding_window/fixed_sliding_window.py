nums = [5, 3, 1, -4, 7, 9]
k = 3

sum = 0
max_sum = 0

for i in range(k):
    sum += nums[i]

max_sum = sum  #dont forget this for same size arr len as k case

for i in range(k, len(nums)):
    sum += nums[i] - nums[i - k]
    max_sum = max(max_sum, sum)

print(max_sum)  #12