# 76. Minimum Window Substring

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.

# 1. Understanding the Question (Simple Words)

# You are given:

# s → big string
# t → target string

# 🎯 Goal:
# Find the smallest substring of s that contains:

# All characters of t
# Including duplicates
# 🔍 Example
# s = "ADOBECODEBANC"
# t = "ABC"

# 👉 Answer = "BANC"
# Because it is the smallest substring containing A, B, C

# 💡 2. Brute Force Approach
# Idea:
# Try all substrings
# Check if it contains all characters of t
# ❌ Problem:
# Time = O(n³) (very slow)
# 🚀 3. Optimal Approach (Sliding Window)
# 🔑 Key Idea

# 👉 We need:

# smallest window that contains all characters of t
# 🔥 Important Concept

# We track:

# need → characters required
# have → characters we have in window

# 👉 When:

# have == need

# ➡️ Window is valid

# 📌 4. Algorithm (Step-by-Step)
# Create frequency map for t
# Initialize:
# left = 0
# have = 0
# need = number of unique chars in t
# min_len = infinity
# Expand window (right):
# Add character to window
# If matches required frequency → have++
# When have == need:
# Window is valid ✅
# Try shrinking from left to make it minimum
# Update answer

def minWindow(s, t):
    if len(t) > len(s):
        return ""
    
    count_t = {}
    for ch in t:
        if ch in count_t:
            count_t[ch] += 1
        else:
            count_t[ch] = 1

    have = 0
    need = len(count_t)
    window = {}
    
    left = 0
    min_len = float("inf")
    result = ""

    for right in range(len(s)):
        ch = s[right]

        if ch in window:
            window[ch] += 1
        else:
            window[ch] = 1

        # check match
        if ch in count_t and window[ch] == count_t[ch]:
            have += 1
        # shrink window
        while have == need:
            if (right - left + 1) < min_len:
                min_len = right - left + 1
                result = s[left : right + 1]

            # remove left char
            left_char = s[left]
            window[left_char] -= 1

            if left_char in count_t and window[left_char] < count_t[left_char]:
                have -= 1

            left += 1

    return result

print(minWindow("ADOBECODEBANC", "ABC"))
print(minWindow("a", "a"))
print(minWindow("a","aa"))


























    