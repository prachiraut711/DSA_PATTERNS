# 35. Search Insert Position

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

# ✅ Idea

# If element not found → return where it should be inserted.

# 🧠 Approach
# Use binary search
# If not found → return left pointer

#yat simply same binary search vala code takycha fakt last la return left karych insert sathi
def searchInsert(nums, target):
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

    return left  #for where to insert position return left

print(searchInsert([1,3,5,6], 5))  #2
print(searchInsert([1,3,5,6], 2))  #1  
print(searchInsert([1,3,5,6], 7))   #4

# Example
# nums = [1,3,5,6]
# target = 2

# Steps:

# mid = 1 → 3 > 2 → go left
# insert position = index 1

# Answer = 1