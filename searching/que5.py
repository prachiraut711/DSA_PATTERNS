# Count number of occurrences (or frequency) in a sorted array
# Last Updated : 3 Oct, 2025
# Given a sorted array arr[] and an integer target, find the number of occurrences of target in given array.

# Examples:

# Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 2
# Output: 4
# Explanation: 2 occurs 4 times in the given array.

# Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 4
# Output: 0
# Explanation: 4 is not present in the given array.

# so here the count aproch will be O(n) linear search so we want more optimal approch

# ✅ Idea

# Count = last index - first index + 1

# 🧠 Approach
# Find first occurrence
# Find last occurrence
# Apply formula

def countOccurrences(nums, target):
    def findFirst():
        left = 0
        right = len(nums) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                ans = mid
                right = mid - 1
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
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return ans
    
    first_index = findFirst()
    last_index = findLast()

    if first_index == -1:
        return 0
    
    return last_index - first_index + 1
 
print(countOccurrences([1, 1, 2, 2, 2, 2, 3], 2))  #4 
print(countOccurrences([1, 1, 2, 2, 2, 2, 3], 4))   #0
print(countOccurrences([1,2,2,2,3,4], 2))  #3

# nums = [1,2,2,2,3,4]
# target = 2
# First index = 1
# Last index = 3

# Count = 3 - 1 + 1 = 3