# 1248. Count Number of Nice Subarrays

# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

# Return the number of nice sub-arrays.

 
# Example 1:

# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
# Example 2:

# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There are no odd numbers in the array.
# Example 3:

# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16

# Question

# Count subarrays containing exactly k odd numbers.

# 🔥 KEY TRICK

# Transform array:

# odd  → 1
# even → 0

# Now problem becomes:

# 👉 Count subarrays with sum = k

# Which becomes SAME as:
# (LeetCode 560 Subarray Sum Equals K)

def numberOfSubarrays(nums, k):
    count = {0 : 1}
    curr_sum = 0
    result = 0

    for num in nums:
        if num % 2 == 1:
            curr_sum += 1

        if curr_sum - k in count:
            result += count[curr_sum - k]

        if curr_sum in count:
            count[curr_sum] += 1
        else:
            count[curr_sum] = 1

    return result

print(numberOfSubarrays([1,1,2,1,1], 3))
print(numberOfSubarrays([2,4,6], 1))
print(numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2))