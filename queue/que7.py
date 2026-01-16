# Stream First Non-repeating
# Given a string s consisting of only lowercase alphabets, for each index i in the string (0 ≤ i < n), find the first non-repeating character in the prefix s[0..i]. If no such character exists, use '#'.

# Examples:

# Input: s = "aabc"
# Output: a#bb
# Explanation: 
# At i=0 ("a"): First non-repeating character is 'a'.
# At i=1 ("aa"): No non-repeating character, so '#'.
# At i=2 ("aab"): First non-repeating character is 'b'.
# At i=3 ("aabc"): Non-repeating characters are 'b' and 'c'; 'b' appeared first, so 'b'. 
# Input: s = "bb" 
# Output: "b#" 
# Explanation: 
# At i=0 ("b"): First non-repeating character is 'b'.
# At i=1 ("bb"): No non-repeating character, so '#'.
# Constraints:
# 1 ≤ s.size() ≤ 105


# We use two data structures:

# Frequency array (size 26)
# → To know how many times a character has appeared.

# Queue
# → To keep characters in the order they arrive.

#O(n)
from collections import deque
def FirstNonRepeating(s):
    freq = [0] * 26
    q = deque()
    ans = []

    for i in s:
        idx = ord(i) - ord("a")   #“ord(ch) - ord('a') converts a lowercase letter into a 0-based index.”
        freq[idx] += 1
        q.append(i)

        while q and freq[ord(q[0]) - ord("a")] > 1:
            q.popleft()
        
        if q:
            ans.append(q[0])
        else:
            ans.append("#")
    
    return "".join(ans)

print(FirstNonRepeating("aabc"))
print(FirstNonRepeating("bb"))

# Why do we subtract ord('a')?

# We want to map characters 'a' to 'z' → indexes 0 to 25

# Character	ASCII	 idx = ord(ch) - ord('a')
# 'a'	     97	           97 - 97 = 0
# 'b'	     98	           98 - 97 = 1
# 'c'	     99	           99 - 97 = 2
# 'z'	    122            122 - 97 = 25

# Example 1
# Input
# A = "aabc"

# Output
# "a#bb"

# 🔍 Dry Run (VERY Detailed)
# Initial State
# freq = [0,0,0,...]
# queue = []
# answer = ""

# Step 1 → char = 'a'
# freq[a] = 1
# queue = [a]

# queue front = 'a' (freq = 1)
# answer = "a"

# Step 2 → char = 'a'
# freq[a] = 2
# queue = [a, a]

# Remove 'a' → freq > 1
# Remove 'a' → freq > 1

# queue = []
# answer = "a#"

# Step 3 → char = 'b'
# freq[b] = 1
# queue = [b]

# queue front = 'b'
# answer = "a#b"

# Step 4 → char = 'c'
# freq[c] = 1
# queue = [b, c]

# queue front = 'b'
# answer = "a#bb"

# 🔹 Example 2 (Important Edge Case)
# Input
# A = "zz"

# Dry Run
# z → freq=1 → answer=z
# z → freq=2 → queue empty → answer=#

# Output
# "z#"

# 🔹 Example 3 (All Unique)
# Input
# A = "abc"

# Output
# "aaa"


# ✔ First non-repeating always remains 'a'

# 🔹 Example 4 (All Repeating)
# Input
# A = "aabbcc"

# Output
# "a#b#c#"

# 🔹 Why This Passes ALL Test Cases

# ✔ Handles:

# repeating characters

# empty queue condition

# continuous stream

# correct GFG output format (#)

# ✔ Time Complexity: O(n)
# ✔ Space Complexity: O(1)

# 🧠 Interview One-Line Explanation

# “We maintain character frequency and a queue; repeating characters are removed from the front until a valid non-repeating character is found.”