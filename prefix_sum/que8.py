# Maximum Size Subarray Sum Equals K / longest subarray sum equals k

# (LeetCode 325 Maximum Size Subarray Sum Equals K)

# 🧠 Problem Statement

# Given an integer array nums and an integer k,

# return the maximum length of a contiguous subarray whose sum equals k.

# If no such subarray exists, return 0.

# A subarray means:

# continuous elements
# 🔹 Example 1
# Input:
# nums = [1,-1,5,-2,3]
# k = 3

# Output:
# 4
# ✅ Explanation

# Subarray:

# [1,-1,5,-2]

# Sum:

# 1 + (-1) + 5 + (-2) = 3

# Length:

# 4

# This is the longest valid subarray.

# 🔹 Example 2
# Input:
# nums = [-2,-1,2,1]
# k = 1

# Output:
# 2
# ✅ Explanation

# Subarray:

# [-1,2]

# Sum:

# 1

# Length:

# 2
# 🔹 Constraints
# 1 <= nums.length <= 2 * 10^5

# -10^4 <= nums[i] <= 10^4

# -10^9 <= k <= 10^9
# 🔥 Interview Important Observation

# Array contains:

# negative numbers

# So:
# ❌ Sliding window will NOT work.

# Because sum can increase/decrease unpredictably.

# So we use:

# Prefix Sum + HashMap
# 🔹 Main Logic

# Suppose:

# current_sum = prefix sum till index i

# If:

# current_sum - k

# already existed before,

# then:

# subarray sum = k
# 🔥 Formula

# If:

# prefix[j] - prefix[i] = k

# Then:

# prefix[i] = prefix[j] - k

# That’s the whole trick.

# 🔹 Algorithm

# Create hashmap:

# prefix_sum → first index
# Traverse array
# Keep updating prefix sum

# Check:

# current_sum - k

# exists or not

# Calculate subarray length
# Store ONLY first occurrence of prefix sum
# (to get maximum length)

def maxSubArrayLen(nums, k):
    prefix_map = {}
    curr_sum = 0
    max_len = 0

    for i in range(len(nums)):
        curr_sum += nums[i]
        
        # if sum from 0 to i equals k
        if curr_sum == k:
            max_len = i + 1   #as index start from 0 to n so +1 
        
        # check if (current_sum - k) exists
        if curr_sum - k in prefix_map:
            length = i - prefix_map[curr_sum - k]
            if length > max_len:
                max_len = length
        
        #store 1st occurance only
        if curr_sum not in prefix_map:
            prefix_map[curr_sum] = i

    return max_len

print(maxSubArrayLen([1,-1,5,-2,3], 3)) #4
print(maxSubArrayLen([-2,-1,2,1], 1)) #2

# Dry Run (VERY IMPORTANT)
# Input
# nums = [1,-1,5,-2,3]
# k = 3
# Step 1
# i = 0
# current_sum = 1

# Check:

# 1 - 3 = -2

# Not found.

# Store:

# prefix_map = {1:0}
# Step 2
# i = 1
# current_sum = 0

# Check:

# 0 - 3 = -3

# Not found.

# Store:

# prefix_map = {1:0, 0:1}
# Step 3
# i = 2
# current_sum = 5

# Check:

# 5 - 3 = 2

# Not found.

# Store:

# prefix_map = {1:0, 0:1, 5:2}
# Step 4
# i = 3
# current_sum = 3

# Now:

# current_sum == k

# So:

# max_len = 4

# Subarray:

# [1,-1,5,-2]
# Step 5
# i = 4
# current_sum = 6

# Check:

# 6 - 3 = 3

# 3 not in hashmap.

# Store:

# {1:0,0:1,5:2,6:4}
# ✅ Final Answer
# 4
# 🔥 Why Store First Occurrence Only?

# Suppose same prefix sum appears multiple times.

# We want:

# maximum length

# So we keep earliest index.

# Because:

# later index - earliest index

# gives bigger length.

# ⏱ Complexity
# Complexity	Value
# Time	O(n)
# Space	O(n)