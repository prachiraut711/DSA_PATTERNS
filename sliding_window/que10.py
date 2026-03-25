# 1004. Max Consecutive Ones III

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


# You are given:
# A binary array → only 0 and 1
# An integer k → you can flip at most k zeros → ones

# 🎯 Goal:
# Find the maximum number of consecutive 1s after flipping ≤ k zeros

# 🔍 Example
# nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2

# 👉 Flip 2 zeros → get longest continuous 1s

# ✅ Output = 6

# 💡 2. Brute Force Approach
# Idea:
# Try all subarrays
# Count number of zeros
# If zeros ≤ k → valid
# Track max length
# Complexity:
# Time: O(n²) ❌ too slow
# 🚀 3. Optimal Approach (Sliding Window)
# 🔑 Key Idea

# 👉 Treat 0 as “bad element”

# We allow:

# at most k zeros in window
# Condition:
# number_of_zeros <= k

# If > k → shrink window

# 📌 4. Algorithm (Step-by-Step)
# Initialize:
# left = 0
# zero_count = 0
# max_len = 0
# Loop right from 0 → n:
# If nums[right] == 0 → increase zero_count
# If zero_count > k:
# Shrink window
# If nums[left] == 0 → decrease zero_count
# Move left
# Update answer:
# max_len = max(max_len, right - left + 1)


def longestOnes(nums, k):
    left = 0
    max_len = 0
    zero_count = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        max_len = max(max_len, right - left + 1)
    
    return max_len

print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))

# Complexity
# Time: O(n)
# Space: O(1)