# 905. Sort Array By Parity

# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
# Return any array that satisfies this condition.

# Example 1:
# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

# Example 2:
# Input: nums = [0]
# Output: [0]

# Approach → Two Pointers

# 👉 Idea:

# Left side → should contain EVEN
# Right side → should contain ODD
# 🔁 Step-by-Step Logic
# left = 0, right = n-1
# Check:
# If left is odd & right is even → swap
# Move pointers:
# If left is even → left++
# If right is odd → right--

# Complexity
# Time: O(n)
# Space: O(1) (in-place)

#Approxh 1 using two pointers
def sortArrayByParity(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] % 2 > nums[right] % 2:   #here we have to check if left is odd and right is even so when % 2 if it gives 1 (odd) > 0(even) so ofcoucorse left is odd and right is even so swap
            nums[left] , nums[right] = nums[right], nums[left]

        if nums[left] % 2 == 0:  #if left is even
            left += 1
        
        if nums[right] % 2 == 1:  #if right is odd
            right -= 1

    return nums

print(sortArrayByParity([3,1,2,4]))   #[4, 2, 1, 3]
print(sortArrayByParity([0]))   #0

#approch 2 using 
