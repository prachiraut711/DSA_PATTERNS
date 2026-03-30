# 201. Bitwise AND of Numbers Range

# Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

# Example 1:

# Input: left = 5, right = 7
# Output: 4
# Example 2:

# Input: left = 0, right = 0
# Output: 0
# Example 3:

# Input: left = 1, right = 2147483647
# Output: 0

# Problem

# 👉 Given two numbers left and right
# 👉 Find:

# left & (left+1) & (left+2) & ... & right
# Example:
# left = 5
# right = 7
# 5 = 101
# 6 = 110
# 7 = 111
# -----------
# AND = 100 = 4
# 🧠 Key Insight (MOST IMPORTANT) ⭐🔥

# 👉 When numbers increase, right-side bits keep changing

# 👉 So:

# Only common left prefix remains
# All changing bits → become 0

# Why This Works

# 👉 We remove non-common bits from right side

# 👉 Only keep:

# common prefix of left and right
# 🟢 Optimal Approach (Shift Method)
def rangeBitwiseAnd(left, right):
    shift = 0

    while left != right:
        left >>= 1   #right shift(>>) => n >> k = n / (2^k)
        right >>= 1  #right shift(>>) => n >> k = n / (2^k)
        shift += 1

    return left << shift    #left shift(<<) => n << k = n * (2^k)

print(rangeBitwiseAnd(5, 7))  #4
print(rangeBitwiseAnd(0, 0))  #0
print(rangeBitwiseAnd(1, 2147483647))  #0

print("_______")
# Alternative (Brian Kernighan Trick)
# 👉 Same idea using:
# right = right & (right - 1)

def rangeBitwiseAnd(left, right):
    while right > left:
        right = right & (right - 1)

    return right

print(rangeBitwiseAnd(5, 7))  #4
print(rangeBitwiseAnd(0, 0))  #0
print(rangeBitwiseAnd(1, 2147483647))  #0