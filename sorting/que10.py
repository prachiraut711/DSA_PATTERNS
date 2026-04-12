# Sort Array by Frequency

# 1636. Sort Array by Increasing Frequency

# Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.
# Return the sorted array.

# Example 1:

# Input: nums = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

# Example 2:
# Input: nums = [2,3,1,3,2]
# Output: [1,3,3,2,2]
# Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

# Example 3:
# Input: nums = [-1,1,-6,4,5,-6,1,4,1]
# Output: [5,-1,4,4,-6,-6,1,1,1]


# Problem
# Sort based on:
# Frequency ↑ (ascending)
# Value ↓ (descending)
# Example
# Input:  [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]

# Why?

# 3 → freq 1 (smallest → comes first)
# 1 → freq 2
# 2 → freq 3
# 🧠 Approach → HashMap + Sorting
# 🔁 Step-by-Step
# Step 1: Count frequency
# count = {1:2, 2:3, 3:1}
# Step 2: Sort with custom rule
# sorted(nums, key=lambda x: (count[x], -x))

# 👉 Meaning:

# First sort by frequency (count[x])
# If tie → larger number first (-x)

from collections import Counter
def sortByFrequency(nums):
    count = Counter(nums)
    return sorted(nums, key=lambda x : (count[x], -x))

print(sortByFrequency([1,1,2,2,2,3]))  #[3, 1, 1, 2, 2, 2]
print(sortByFrequency([1,1,2,2,3,3]))  # [3, 3, 2, 2, 1, 1]   for thi type of ex. of tie we use (-x) larger number first 

# Example Walkthrough

# Input:

# [1,1,2,2,2,3]

# Mapped:

# 1 → 2
# 2 → 3
# 3 → 1

# Sorting rule:

# (freq, -value)

# So:

# 3 → (1, -3)
# 1 → (2, -1)
# 2 → (3, -2)

# Final:

# [3,1,1,2,2,2] ✅
# ⏱ Complexity
# Time: O(n log n)
# Space: O(n)
# 🔥 DIFFERENCE (VERY IMPORTANT)
# Feature	Parity Sort	Frequency Sort
# Concept	Partitioning	Sorting + Hashing
# Technique	Two pointers	Custom sort
# Space	O(1)	O(n)
# Time	O(n)	O(n log n)
# ⚡ Interview Tip

# 👉 If problem says:

# “even/odd”, “positive/negative” → Two pointers
# “frequency”, “top k”, “count” → HashMap + Heap/Sort