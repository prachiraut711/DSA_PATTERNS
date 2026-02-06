# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

# 🔹 What the Question Wants (in simple words)

# Given a string s:

# 👉 Find the length of the longest contiguous substring
# 👉 such that no character repeats

# ❌ Subsequence is NOT allowed
# ✅ Only continuous characters

# 🔹 Key Idea (Pattern)

# This is a Sliding Window problem.

# Why?

# We want a continuous window

# We expand the window when characters are unique

# We shrink the window when a duplicate appears

# To track duplicates efficiently → use a set

# 🔹 Algorithm (Very Clear)

# Initialize:

# left = 0

# char_set = set()

# max_len = 0

# Move right pointer from 0 to len(s)-1

# If s[right] is already in char_set:

# Remove s[left] from set

# Move left forward

# Repeat until duplicate is gone

# Add s[right] to set

# Update max_len = max(max_len, right - left + 1)

# Return max_len

def lengthOfLongestSubstring(s):
    left = 0
    max_len = 0
    seen = set()

    for right in range(len(s)):
        while s[right] in seen: # while is imp if put if condition it will be wrong
            seen.remove(s[left])
            left += 1
        
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)   #r-l+1 kel tarch corect len bethtiye index chi 

    return max_len

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))