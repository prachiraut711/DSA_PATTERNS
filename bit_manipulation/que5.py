# 136. Single Number

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:

# Input: nums = [2,2,1]

# Output: 1

# Example 2:

# Input: nums = [4,1,2,1,2]

# Output: 4

# Example 3:

# Input: nums = [1]
# Output: 1


# Given an array where:

# Every element appears twice
# Only one element appears once

# 👉 Return that single element

# Example:
# nums = [2, 2, 1]
# Output = 1
# 🧠 Key Idea (XOR Trick) ⭐🔥

# 👉 Use:

# a ^ a = 0  
# a ^ 0 = a

# 👉 So:

# Duplicate numbers cancel out
# Only unique number remains

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num

    return result

print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))