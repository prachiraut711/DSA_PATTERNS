# 523. Continuous Subarray Sum

# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

# A good subarray is a subarray where:

# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:

# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

# Example 1:

# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
# Example 2:

# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
# Example 3:

# Input: nums = [23,2,6,4,7], k = 13
# Output: false

# 🧠 Question

# Check if there exists a subarray:

# length ≥ 2
# whose sum is divisible by k
# 💡 Main Logic

# If:

# prefix_sum % k repeats

# then subarray sum between them is divisible by k.

# 🔥 Important Math

# If:

# a % k == b % k

# Then:

# (a - b) % k == 0

# That means divisible by k.

# ⚙️ Algorithm

# Store:

# remainder → first index

# If same remainder appears again:

# subarray between them divisible by k


#ithe remainder and tyache index store kele because aplyla lenght check karchiye 2 peksha mothi ahe ka te 
# so by storing index we do curr_index - remainder_insdex to get lenght
def checkSubarraySum(nums, k):
    remainder_map = {0 : -1}  #ithe index store kartey so mag initilize remainder 0 and its index -1 (as array starts with 0,1...)
    curr_sum = 0

    for i in range(len(nums)):
        curr_sum += nums[i]

        remainder = curr_sum % k

        if remainder in remainder_map:
            if i - remainder_map[remainder] >= 2:
                return True
        else:
            remainder_map[remainder] = i

        
    return False

print(checkSubarraySum([23,2,4,6,7], 6))
print(checkSubarraySum([23,2,6,4,7], 6))
print(checkSubarraySum([23,2,6,4,7], 13))



# Example
# nums = [23,2,4,6,7]
# k = 6

# Prefix sums:

# 23 → 5
# 25 → 1
# 29 → 5   ← repeated

# Same remainder 5 repeated
# ⇒ subarray between them divisible by 6