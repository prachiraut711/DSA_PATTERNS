# https://leetcode.com/problems/longest-palindromic-substring/

# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"

def longestPalindrome(s):
    res = ""

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]    #left + 1 kel bcz atta varti left -1 kel na ani jar same nasel s[left] == s[right] tar lest chya pudun s banli

    for i in range(len(s)):
        p1 = expand(i, i)    #for odd len
        p2 = expand(i, i+1)  #for even len
        res = max(res, p1, p2, key=len)   # key=len => “Compare these strings based on their length, not alphabetically.”
    
    return res

print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))