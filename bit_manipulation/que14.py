# 190. Reverse Bits

# Reverse bits of a given 32 bits signed integer.

# Example 1:
# Input: n = 43261596
# Output: 964176192
# Explanation:
# Integer	Binary
# 43261596	00000010100101000001111010011100
# 964176192	00111001011110000010100101000000

# Example 2:
# Input: n = 2147483644
# Output: 1073741822
# Explanation:
# Integer	    Binary
# 2147483644	01111111111111111111111111111100
# 1073741822	00111111111111111111111111111110

# Constraints:
# 0 <= n <= 231 - 2
# n is even.


# Key Idea

# 👉 Take bits from right → build result from left

# Extract last bit → (n & 1)
# Shift result left
# Shift n right

def reverseBits(n):
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)  #2. OR Operator |  👉 Rule: If any one is 1 → result is 1 
        n >>= 1
    return result

print(reverseBits(43261596))
print(reverseBits(2147483644))
#“Take last bit of n and keep adding it to result from left”

# Step-by-Step (Simple Example)

# 👉 Let’s take small number:

# n = 5 → 101

# Steps:

# result = 0

# Step 1:
# result = (0 << 1) | 1 = 1
# n = 10

# Step 2:
# result = (1 << 1) | 0 = 10
# n = 1

# Step 3:
# result = (10 << 1) | 1 = 101

# 👉 Reversed → same here (but works for full 32-bit)

# ⚡ Important Line
# result = (result << 1) | (n & 1)

# 👉 Meaning:

# Shift result left
# Add last bit of n
# 🟡 Alternative (String Way – Not Preferred)
# def reverseBits(n):
#     b = bin(n)[2:].zfill(32)
#     return int(b[::-1], 2)

# ⛔ Not good for interviews (uses built-in)

# ⚡ Complexity
# Time: O(32) → O(1)
# Space: O(1)
# 🔥 Interview Tips

# 👉 Always mention:

# “We process 32 bits”
# “Use bit extraction and shifting”

# 👉 Keywords to say:

# n & 1 → get last bit
# << → build reversed number
# >> → move input
# 🚀 Pattern Connection

# This connects with:

# Count bits
# Bit shifting
# Binary manipulation

# ⚡ One-Line Idea

# 👉 “Take last bit of n and keep adding it to result from left”