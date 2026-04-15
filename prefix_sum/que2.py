# 303. Range Sum Query - Immutable

# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 
# Example 1:

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]

# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

# Question

# You are given an array nums. You need to answer multiple queries like:

# 👉 “What is sum from index left to right?”

# 💡 Idea

# Instead of calculating sum every time (O(n)), we precompute prefix sum.

# ⚙️ Algorithm
# Create prefix array prefix
# prefix[i] = sum of elements from 0 to i

# For query:

# sum(left, right) = prefix[right] - prefix[left-1]

class numArray(object):

    def __init__(self, nums):
        self.prefix = [0] * len(nums)
        self.prefix[0] = nums[0]

        for i in range(1, len(nums)):
            self.prefix[i] = self.prefix[i - 1] + nums[i]

    def sumRange(self, left, right):
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]
    
# ✅ Create object
obj = numArray([1, 2, 3, 4])

# ✅ Call method using object
print(obj.sumRange(0, 2))   #6
print(obj.sumRange(1, 3))  #9

# Example
# nums = [1, 2, 3, 4]

# prefix = [1, 3, 6, 10]

# Query: sum(1,3)
# = 10 - 1 = 9

        
        