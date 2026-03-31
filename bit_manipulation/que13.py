# 338. Counting Bits

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

#approch 1
def setBits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def countBits(n):
    res = []
    for i in range(n + 1):
        res.append(setBits(i))
    return res

print(countBits(2))  #[0,1,1]
print(countBits(5))  #[0,1,1,2,1,2]
print("____")
#approch 2 :OPTIMAL APPROCH
# Optimal Approach (DP + Bit Trick)
# ✅ Formula
# ans[i] = ans[i & (i - 1)] + 1
# 🧠 Why This Works
# 👉 We know:
# i & (i - 1)
# removes the last set bit
# So:
# bits(i) = bits(i without last 1) + 1
# Step-by-Step Example
# i = 5
# 5 = 101
# i & (i-1) = 101 & 100 = 100 (4)
# So:
# ans[5] = ans[4] + 1 = 1 + 1 = 2

def countBits(n):
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i & (i - 1)] + 1
    return ans

print(countBits(2))  #[0,1,1]
print(countBits(5))  #[0,1,1,2,1,2]
print("____")
# 👉 Alternative DP (VERY EASY TO UNDERSTAND)
# Formula:
# ans[i] = ans[i // 2] + (i & 1)

# 👉 Explanation:

# i // 2 → removes last bit
# (i & 1) → checks last bit

# ✅ Code
def countBits(n):
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i // 2] + (i & 1)
    return ans

print(countBits(2))  #[0,1,1]
print(countBits(5))  #[0,1,1,2,1,2]
# 🔍 Example
# For i = 5:
# 5 // 2 = 2 → ans[2] = 1
# 5 & 1 = 1

# 👉 ans[5] = 1 + 1 = 2

# ⚡ Complexity
# Time: O(n) ✅ (required by problem)
# Space: O(n)

# 👉 Better than brute force O(n log n)

# 🔥 Interview Tips

# 👉 Say this:

# “I’ll use DP + bit manipulation”
# “Use previously computed results”
# Mention:
# i & (i - 1)
# 🚀 Final Summary
# Method	Idea	Use
# Brute force	Count bits each time	❌
# DP (i//2)	Shift + last bit	✅ Easy
# DP (i&(i-1)) ⭐	Remove last set bit	🔥 Best