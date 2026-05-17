# 238. Product of Array Except Self
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Because:
# For index 0:
# 2×3×4 = 24

# For index 1:
# 1×3×4 = 12

# For index 2:
# 1×2×4 = 8

# For index 3:
# 1×2×3 = 6


# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

def productExceptSelf(nums):
    left = []
    for i in range(len(nums)):
        if i == 0:
            left.append(1)
        else:
            left.append(nums[i - 1] * left[-1])

    right = []
    for i in range(len(nums) - 1, -1, -1):
        if i == len(nums) - 1:
            right.insert(0, 1)
        else:
            right.insert(0, nums[i + 1] * right[0])

    ans = []
    for i in range(len(nums)):
        ans.append(left[i] * right[i])
    
    return ans

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))