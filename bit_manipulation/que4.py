# 231. Power of Two

# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

# Example 1:

# Input: n = 1
# Output: true
# Explanation: 2^0 = 1
# Example 2:

# Input: n = 16
# Output: true
# Explanation: 2^4 = 16
# Example 3:

# Input: n = 3
# Output: false

# Given an integer n, return True if it is a power of 2.

# 👉 Examples:

# 1 → ✅ (2⁰)
# 2 → ✅ (2¹)
# 4 → ✅ (2²)
# 6 → ❌
# 🧠 Key Idea (MOST IMPORTANT)

# 👉 Power of 2 numbers have only ONE set bit

# Examples:

# 1  = 0001
# 2  = 0010
# 4  = 0100
# 8  = 1000
#Optimal Solution
def isPowerOfTwo(n):
    if n <= 0:
        return False
    
    return n & (n - 1) == 0

print(isPowerOfTwo(1))
print(isPowerOfTwo(4))
print(isPowerOfTwo(3))

print("__________")

def isPowerOfTwo(n):
    if n <= 0:
        return False
    
    while n % 2 == 0:
        n = n // 2

    return n == 1

print(isPowerOfTwo(1))
print(isPowerOfTwo(4))
print(isPowerOfTwo(3))