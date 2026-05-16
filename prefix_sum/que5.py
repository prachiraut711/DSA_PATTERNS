# 930. Binary Subarrays With Sum

# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

# A subarray is a contiguous part of the array.
# Example 1:

# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]

# Example 2:
# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# nums[i] is either 0 or 1.
# 0 <= goal <= nums.length


def binarySubarraySum(nums, goal):
    count = {0 : 1}
    current_sum = 0
    result = 0

    for num in nums:
        current_sum += num

        if current_sum - goal in count:
            result += count[current_sum - goal]

        if current_sum in count:
            count[current_sum] += 1
        else:
            count[current_sum] = 1

    return result

print(binarySubarraySum([1,0,1,0,1], 2))
print(binarySubarraySum([0,0,0,0,0], 0))
