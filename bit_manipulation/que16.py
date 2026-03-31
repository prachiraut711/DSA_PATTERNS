# Problem: Check if Number is Power of Four

# 👉 Return True if:

# n = 4^x   (x ≥ 0)
# Examples:
# 1 → ✅ (4⁰)
# 4 → ✅ (4¹)
# 16 → ✅ (4²)
# 8 → ❌

# 🧠 Key Idea (IMPORTANT) ⭐🔥

# A number is power of 4 if:

# ✅ 1. It is power of 2
# n & (n - 1) == 0
# ✅ 2. Its set bit is at even position

# 👉 Because:

# 4^0 = 1   → position 0
# 4^1 = 100 → position 2
# 4^2 = 10000 → position 4

# 👉 Always even index (0-based)

# 🟢 Optimal Solution ⭐
def powerOfFour(n):
    if n <= 0:
        return False
    
    return (n & (n - 1) == 0) and (n & 0x55555555) != 0   #pahile power of 2 he ka bagitl and even position bits ahe ka bagitl

print(powerOfFour(16))  #true
print(powerOfFour(8))  #false

# Why 0x55555555?
# 👉 Binary:
# 01010101010101010101010101010101
# 👉 It keeps only even position bits
print("_________")
#alternative math approch
def powerOfFour(n):
    if n <= 0:
        return False
    
    while n % 4 == 0:
        n //= 4

    return n == 1

print(powerOfFour(16))  #true
print(powerOfFour(8))  #false
# ⚡ Example
# n = 16
# 16 = 10000
# Power of 2? ✅
# Even position? ✅

# 👉 TRUE

# n = 8
# 8 = 1000
# Power of 2? ✅
# Even position? ❌

# 👉 FALSE

# ⚡ Complexity
# Time: O(1)
# Space: O(1)
# 🔥 Interview Tips

# 👉 Say this:

# “First check power of 2”
# “Then ensure bit is at even position using mask”
# 🚀 One-Line Version
# return n > 0 and (n & (n-1)) == 0 and (n & 0x55555555)
# 🧠 Pattern Connection
# Power of 2
# Bit masking
# Position-based bit checking
# 🎯 Final Insight

# 👉 All powers of 4 are powers of 2, but not all powers of 2 are powers of 4
