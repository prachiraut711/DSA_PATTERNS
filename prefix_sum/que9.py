# 53. Maximum Subarray

# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

# 🔥 VERY VERY IMPORTANT
# Asked in almost every company.

# 🧠 Question

# Find the:

# maximum possible sum of a contiguous subarray
# 🔍 Example
# nums = [-2,1,-3,4,-1,2,1,-5,4]

# Best subarray:

# [4,-1,2,1]

# Sum:

# 6
# 💡 Main Idea (Kadane’s Algorithm)

# At every index:

# either continue previous subarray
# or start new subarray
# ⚙️ Algorithm

# For each number:

# current_sum = max(num, current_sum + num)

# Then:

# answer = max(answer, current_sum)

# Easy Memory Trick

# If previous sum becomes bad:

# start fresh
# ⏱ Complexity
# Time	O(n)
# Space	O(1)

def maxSubArray(nums):
    curr_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])

        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  #6
print(maxSubArray([1]))  #1
print(maxSubArray([5,4,-1,7,8]))  #23

print('___________')
#other method

def maxSubArray(nums):
    max_sum = float("-inf")
    curr_sum = 0

    for i in nums:
        curr_sum += i
        max_sum = max(max_sum, curr_sum)

        if curr_sum < 0:
            curr_sum = 0

    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  #6
print(maxSubArray([1]))  #1
print(maxSubArray([5,4,-1,7,8]))  #23