# Toggle the i-th Bit
# 🧠 Idea

# 👉 Toggle means:

# 0 → 1
# 1 → 0

# 👉 Use:

# n ^ (1 << i)

# Example
# 👉 n = 5 → 101, toggle bit at i = 1

# 1 << 1 = 010
# ------------
# 101
# 010
# ----
# 111 = 7

def toggle_ith_bit(n, i):
    return n ^ (1 << i)

print(toggle_ith_bit(5, 1))  # 7

# ⚡ Quick Summary
# Operation	Formula
# Check bit	n & (1 << i)
# Clear bit	n & ~(1 << i)
# Toggle bit	n ^ (1 << i)