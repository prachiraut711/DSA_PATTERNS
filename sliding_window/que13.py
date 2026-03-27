# 438. Find All Anagrams in a String

# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

# 1. Understanding the Question (Simple Words)

# You are given:

# s → big string
# p → pattern string

# 🎯 Goal:
# Return all starting indices where an anagram of p exists in s

# 🔑 Meaning

# 👉 Find all substrings in s that:

# Have same length as p
# Have same characters (any order)
# 🔍 Example
# s = "cbaebabacd"
# p = "abc"

# Substrings of length 3:

# "cba" → ✅ anagram → index 0
# "bac" → ✅ anagram → index 6

# 👉 Output = [0, 6]

# 💡 2. Brute Force Approach
# Idea:
# Take every substring of size len(p)
# Sort and compare
# sorted(substring) == sorted(p)
# ❌ Problem:
# Sorting every time → slow
# Time: O(n * k log k) ❌
# 🚀 3. Optimal Approach (Sliding Window)
# 🔑 Key Idea

# 👉 Instead of sorting → compare frequency

# 👉 Same as:


# 📌 4. Algorithm (Step-by-Step)
# Create:
# count_p → frequency of p
# count_s → frequency of window
# Loop through s:
# Add right character
# If window > size → remove left
# If both counts equal:
# Add left to result


# Permutation in String → but return ALL indices
# 🔥 Important

# 👉 Window size = len(p) (fixed)


def findAnagrams(s, p):
    result = []

    if len(p) > len(s):
        return []     #here not return False as in question we have to return list of indices
    
    count_p = [0] * 26   #frquency of p string
    count_s = [0] * 26   #frquency of s string

    for ch in p:
        count_p[ord(ch) - ord("a")] += 1

    left = 0
    for right in range(len(s)):
        count_s[ord(s[right]) - ord("a")] += 1

        if right - left + 1 > len(p):
            count_s[ord(s[left]) - ord("a")] -= 1
            left += 1

        if count_p == count_s:
            result.append(left)

    return result

print(findAnagrams("cbaebabacd", "abc"))
print(findAnagrams("abab", "ab"))
