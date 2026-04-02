# 540. Single Element in a Sorted Array

# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: nums = [3,3,7,7,10,11,11]
# Output: 10

# Idea

# All elements appear twice except one.
# Use index pattern (even/odd).

# 🧠 Trick
# Pairs start at even index
# If pattern breaks → single is on left
# 🧠 Approach
# If mid is odd → make it even (mid -= 1)
# Compare nums[mid] and nums[mid+1]

def singleNonDuplicate(nums):
    left, right = 0, len(nums)-1

    while left < right:
        mid = (left + right)//2

        if mid % 2 == 1:
            mid -= 1

        if nums[mid] == nums[mid+1]:
            left = mid + 2    #ithe mid + 2 jar mid + 1 ke tar time limit exceed hoil ani wrong hoil
        else:
            right = mid

    return nums[left]

print(singleNonDuplicate([1,1,2,3,3,4,4,8,8]))   #2
print(singleNonDuplicate([3,3,7,7,10,11,11]))   #10

# Example
# nums = [1,1,2,3,3,4,4,8,8]
# mid = 4 → pair ok → go right
# pattern breaks at 2 → answer = 2