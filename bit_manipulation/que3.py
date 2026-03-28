# # Count Set Bits

# 191. Number of 1 Bits

# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

# Example 1:
# Input: n = 11
# Output: 3
# Explanation:
# The input binary string 1011 has a total of three set bits.

# Example 2:
# Input: n = 128
# Output: 1
# Explanation:
# The input binary string 10000000 has a total of one set bit.

# Example 3:
# Input: n = 2147483645
# Output: 30
# Explanation:
# The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

#A bit is called set if it is 1.

# Method 1: Simple (Loop + Check Last Bit)
def hammingWeight(n):
    count = 0
    while n > 0:
        count += n & 1
        n = n >> 1
    return count

print(hammingWeight(11))
print(hammingWeight(128))
print(hammingWeight(2147483645))
# n & 1 → tells if last bit is 1
# n >> 1 → move to next bit
# ⏱ Complexity
# Time: O(number of bits) → ~32

print("________")

# 🟡 Method 2: OPTIMAL (Brian Kernighan’s Algorithm) ⭐🔥
# 👉 Most important for interviews

# n & (n - 1)
# 👉 This removes the rightmost set bit
def hammingWeight(n):
    count = 0
    while n:
        n = n & (n - 1)
        count += 1
    return count

print(hammingWeight(11))
print(hammingWeight(128))
print(hammingWeight(2147483645))

# n & (n - 1)
# 👉 This removes the rightmost set bit

# ex. n = 10 → 1010
# 1st: 1010 & 1001 = 1000  
# 2nd: 1000 & 0111 = 0000  
# Count = 2

# ⏱ Complexity
# Time: O(number of set bits) ⚡ (FASTER)