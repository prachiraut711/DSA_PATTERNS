# 560. Subarray Sum Equals K

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

def subarraySum(nums, k):
    count = {0 : 1}
    current_sum = 0
    result = 0

    for num in nums:
        current_sum += num

        if current_sum - k in count:
            result += count[current_sum - k]

        if current_sum in count:
            count[current_sum] += 1
        else:
            count[current_sum] = 1

    return result

print(subarraySum([1,1,1], 2))
print(subarraySum([1,2,3], 3))