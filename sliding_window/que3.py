# 643. Maximum Average Subarray I

# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
#  Any answer with a calculation error less than 10-5 will be accepted.
# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:
# Input: nums = [5], k = 1
# Output: 5.00000

# Constraints:
# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104

#jya window chi maximum sum asel tyachich avg max asel na mag max_sum kadh ani tya divide by k kar mag ans yeil
def findMaxAvg(arr, k):
    window_sum = 0
    max_sum = 0

    for i in range(k):
        window_sum += arr[i]
    
    max_sum = window_sum  #dont forget this for same size window as k case

    #to check next window
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    max_avg = max_sum / k   #in leetcode use float(max_sum) / k as leetcode supports Python 2 integer division if not used float then will show error
    return max_avg
#jya window chi maximum sum asel tyachich avg max asel na mag max_sum kadh ani tya divide by k kar mag ans yeil

print(findMaxAvg([1,12,-5,-6,50,3],4))
print(findMaxAvg([5], 1))