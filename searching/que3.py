# 34. Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

# Idea

# Find first occurrence and last occurrence using binary search.

# 🧠 Approach
# Run binary search twice:
# once for first position (yat go left for first occurance)   right = mid - 1
# once for last position  (yat go right for last occurance)  left = mid + 1

def searchRange(nums, target):
    def findFirst():
        left = 0
        right = len(nums) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                ans = mid
                right = mid - 1 #go left(for getting first occurance)  #IMP DONT FORGRT 
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return ans

    def findLast():
        left = 0
        right = len(nums) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                ans = mid
                left = mid + 1  #go right (for getting last occurance)  #IMP DONT FORGRT 
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return ans
    
    return [findFirst(), findLast()]

print(searchRange([5,7,7,8,8,10], 8)) #[3,4]
print(searchRange([5,7,7,8,8,10], 6))  #[-1,-1]
print(searchRange([], 0))    #[-1,-1]

# Example
# nums = [5,7,7,8,8,10]
# target = 8

# Steps:

# First occurrence → index 3
# Last occurrence → index 4

# Answer: [3, 4]