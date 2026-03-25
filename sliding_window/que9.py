# 209. Minimum Size Subarray Sum

# Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

# 2. Brute Force Approach
# Idea:
# Try all subarrays
# Calculate sum
# Check if ≥ target
# Track minimum length
# Code Idea
# for i in range(n):
#     sum = 0
#     for j in range(i, n):
#         sum += nums[j]
#         if sum >= target:
#             update min length
# Complexity:
# Time: O(n²) ❌ too slow
# 🚀 3. Optimal Approach (Sliding Window)

# 👉 Since all numbers are positive, we can use sliding window

# 🔑 Key Idea
# Expand window → increase sum
# Shrink window → reduce size while maintaining condition

# 📌 4. Algorithm (Step-by-Step)
# Initialize:
# left = 0
# sum = 0
# min_len = infinity
# Loop right from 0 → n:
# Add nums[right] to sum
# While sum >= target:
# Update min_len
# Remove nums[left]
# Move left++
# If no valid subarray → return 0


#positive elment ahet mahnun work karen pn negative elmemnt aste tar ha approch chuken

def minSubArrayLen(target, nums):
    left = 0
    min_len = float("inf")    #jar min_len zero getl tar nehmi minimum tar zero ch rahil na mag saglikade ans zero ch yeil  so ithe infinity gyach.
    total = 0

    for right in range(len(nums)):
        total += nums[right]

        while total >= target:
            min_len = min(min_len, right - left + 1)
            total -= nums[left]
            left += 1

    return 0 if min_len == float("inf") else min_len
#jar min_len zero getl tar nehmi minimum tar zero ch rahil jevva  min_len = min(min_len, right - left + 1) he use karu tar mahnun infinity getl ithe
print(minSubArrayLen(7, [2,3,1,2,4,3]))
print(minSubArrayLen(4, [1,4,4]))
print(minSubArrayLen(11, [1,1,1,1,1,1,1,1]))




#  8. Why Sliding Window Works?

# 👉 Because all numbers are positive

# So:

# Expanding → sum increases
# Shrinking → sum decreases

# 👉 This monotonic behavior makes it efficient

# ❗ Important Note

# If array had negative numbers, this approach would ❌ NOT work

# ⏱️ 9. Complexity
# Time: O(n)
# Space: O(1)
# 🔥 10. Pattern Recognition

# 👉 This is a classic:
# “Minimum window / smallest subarray with condition”