# 567. Permutation in String
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

# 1. Understanding the Question (Simple Words)

# You are given:

# s1 → small string
# s2 → big string

# 🎯 Goal:
# Check if any permutation of s1 exists in s2 as a substring

# 🔑 What is permutation?

# Permutation = same characters, different order

# Example:

# s1 = "ab"
# permutations = "ab", "ba"
# 🔍 Example
# s1 = "ab"
# s2 = "eidbaooo"

# 👉 "ba" is inside s2
# 👉 "ba" is permutation of "ab"

# ✅ Answer = True

# 💡 2. Brute Force Approach
# Idea:
# Generate all permutations of s1
# Check if any exists in s2
# ❌ Problem:
# Permutations = n! (factorial) → very slow
# Not usable in interview
# Better brute:
# Check every substring of size len(s1)
# Compare sorted strings
# sorted(s1) == sorted(substring)

# 👉 Time: O(n * k log k) ❌

# 🚀 3. Optimal Approach (Sliding Window)
# 🔑 Key Idea

# 👉 Instead of checking permutations, compare frequency

# 👉 A substring is valid if:

# same character count as s1
# 🔥 Important Trick

# 👉 Window size = len(s1) (fixed)

# 📌 4. Algorithm (Step-by-Step)
# If len(s1) > len(s2) → return False
# Create:
# count1 → frequency of s1
# count2 → frequency of current window
# Loop through s2:
# Add new character to window
# Remove old character (if window too big)

# Compare:

# if count1 == count2:
#     return True


# Key Insight

# 👉 You are NOT finding permutation directly
# 👉 You are matching frequency

#ithe len(s1) was k so sliding window 
def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    
    count1 = [0] * 26    #frequency of s1
    count2 = [0] * 26    #frequency of current window

    for ch in s1:
        count1[ord(ch) - ord("a")] += 1

    left = 0
    for right in range(len(s2)):
        count2[ord(s2[right]) - ord("a")] += 1

        if right - left + 1 > len(s1):
            count2[ord(s2[left]) - ord("a")] -= 1
            left += 1
        
        if count1 == count2:
            return True
        
    return False

print(checkInclusion("ab", "eidbaooo"))
print(checkInclusion("ab", "eidboaoo"))

