# 1. Clear the i-th Bit
# 🧠 Idea

# 👉 We want to make the i-th bit = 0

# 👉 Use:

# n & ~(1 << i)

def clear_ith_bit(n, i):
    return n & ~(1 << i)

print(clear_ith_bit(5, 0)) 
# 🔍 Example

# 👉 n = 5 → 101, clear bit at i = 0

# 1 << 0 = 001
# ~001   = 110
# ------------
# 101
# 110
# ----
# 100 = 4