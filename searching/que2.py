# Binary Search

# Binary search is a more efficient searching algorithm suitable for sorted lists. It repeatedly divides the search interval in half until the target value is found.

# Steps:
# Start with the entire sorted list.
# Compute the middle element of the list.
# If the middle element is equal to the target value, return its index.
# If the middle element is less than the target value, search in the right half of the list.
# If the middle element is greater than the target value, search in the left half of the list.
# Repeat steps 2-5 until the target value is found or the search interval is empty.

# 704. Binary Search
# Easy
# Topics
# premium lock icon
# Companies
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

# Idea

# Works only on sorted array. Divide and conquer.
# 🧠 Approach
# Take middle element
# If target == mid → return
# If target < mid → search left
# If target > mid → search right
# ⏱ Complexity
# Time: O(log n) (very fast)
# Space: O(1)

def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

print(binarySearch([-1,0,3,5,9,12], 9))  #4
print(binarySearch([-1,0,3,5,9,12], 2))  #-1

        