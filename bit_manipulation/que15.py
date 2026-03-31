# Problem: Find XOR of Numbers from 1 to N

# 👉 Compute:

# 1 ^ 2 ^ 3 ^ 4 ^ ... ^ n
# 🧠 Key Insight (MOST IMPORTANT) ⭐🔥

# 👉 XOR from 1 → n follows a pattern based on n % 4

# 🟢 Pattern Table
# n % 4	   Result
# 0	        n
# 1     	1
# 2	        n + 1
# 3	        0

# 🧪 Examples
# n = 4
# 1 ^ 2 ^ 3 ^ 4 = 4
# n = 5
# 1 ^ 2 ^ 3 ^ 4 ^ 5 = 1
# n = 6
# = 7
# n = 7
# = 0

# Brute Force (Don’t use) corect but  # ⛔ Time: O(n)
def xor_1_to_n(n):
    XOR = 0
    for i in range(1, n+1):
        XOR ^= i
    return XOR
print(xor_1_to_n(5))  #1

print("__________")


# 🟢 Optimal Code ⭐
def xor_1_to_n(n):
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    else:
        return 0

print(xor_1_to_n(5))  # 1

print("__________")

# ⚡ One-Line Version
def xor_1_to_n(n):
    return [n, 1, n + 1, 0][n % 4]

print(xor_1_to_n(5))  # 1

# 🔍 Why This Pattern Works

# 👉 XOR cancels values in a repeating cycle:

# 1 ^ 2 ^ 3 ^ 4 = 4
# 5 ^ 6 ^ 7 ^ 8 = 8

# 👉 Pattern repeats every 4 numbers

# 🔥 Interview Tips

# 👉 Say this:

# “XOR from 1 to n follows a repeating pattern of 4”
# “So we can solve in O(1) time”

# 🧠 Bonus

# 👉 XOR from L to R:

# xor(L to R) = xor(1 to R) ^ xor(1 to L-1)