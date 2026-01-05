# 977. Squares of a Sorted Array

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# 💡 Key Observation
# Largest square comes from:

# largest positive number

# OR largest absolute negative number

# These are at the ends of the array.

def sortedSquares(nums):
    left = 0
    right = len(nums) - 1
    res = [0] * len(nums)   # ithe res = [] kel tar error yeil aplyla same size ch hav ahe na nums yedydya mahnun res = [0] * len(nums)
    pos = len(nums) - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            res[pos] = nums[left] *  nums[left]
            left += 1
        else:
            res[pos] = nums[right] * nums[right]
            right -= 1
        pos -= 1

    return res

print(sortedSquares([-4,-1,0,3,10]))
print(sortedSquares([-7,-3,2,3,11]))