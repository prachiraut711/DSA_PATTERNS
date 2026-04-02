# 153. Find Minimum in Rotated Sorted Array

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

# Idea

# Minimum lies in unsorted part

# 🧠 Approach
# If nums[mid] > nums[right] → min in right
# Else → min in left (including mid)

def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:  #ithe single elemnt nums madhun ch pahije so left < right kel not left <= right he mostly target kivva first, second occurance, kivva target asel tar madhe use hot
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid  #logically vichar kar as this nums is rotated so when nums[mid] > nums[right] so the minimum el will be in right sight so left = mid + 1 kel ani jar nasel  he gari right lach min bhetnar na mag right = mid - 1 karun kahi upyog nahi bcz he tar left la zail so mag ithe right = mid kel
        
    return nums[left]   

print(findMin([3,4,5,1,2]))  #1
print(findMin([4,5,6,7,0,1,2]))  #0
print(findMin([11,13,15,17]))  #11
# Example
# nums = [3,4,5,1,2]
# mid = 2 → 5 > 2 → go right
# mid = 3 → 1 ≤ 2 → go left
# answer = 1