
# Code
# Testcase
# Testcase
# Test Result
# 424. Longest Repeating Character Replacement
# Medium
# Topics
# premium lock icon
# Companies
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.

# Key Idea

# We maintain a window and:

# Track most frequent character count

# Check:

# window_size - max_freq <= k

# 👉 If true → valid window
# 👉 Else → shrink window

# 📌 4. Algorithm (Step-by-Step)
# Initialize:
# left = 0
# max_freq = 0
# count[26] = {0}
# max_length = 0
# Loop right from 0 → n:
# Increase count of current char
# Update max_freq

# Check condition:

# if window_size - max_freq > k:
#     shrink window (left++)

# Update answer:

# max_length = max(max_length, window_size)

def characterReplacement(s, k):
    count = [0] * 26
    left = 0
    max_freq = 0
    max_len = 0

    for right in range(len(s)):
        # Increase count of current character
        count[ord(s[right]) - ord("A")] += 1
        
        # Update max frequency
        max_freq = max(max_freq, count[ord(s[right]) - ord("A")])
        
         # Check if window is valid
        while (right - left + 1) - max_freq > k:
            count[ord(s[left]) - ord("A")] -= 1
            left += 1

        # check max length
        max_len = max(max_len, right - left + 1)
    
    return max_len



print(characterReplacement("ABAB", 2))
print(characterReplacement("AABABBA", 1))



#in window_size - max_fre > k condition stiesfy then
# count[ord(s[right]) - ord("A")] -= 1   # ❌ WRONG

# ✅ Correct Line
# count[ord(s[left]) - ord("A")] -= 1   # ✅ CORRECT   left vali ch freq shirnk karychi