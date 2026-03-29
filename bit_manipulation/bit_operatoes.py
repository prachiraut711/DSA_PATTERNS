# 🔢 BITWISE OPERATORS TABLE

# We’ll cover all:
# & , | , ^ , ~ , << , >>

# 🟢 1. AND Operator &
# 👉 Rule: 1 & 1 = 1, otherwise 0

# A	B	A & B
# 0	0	0
# 0	1	0
# 1	0	0
# 1	1	1

# 👉 Example:

# 5 = 101
# 3 = 011
# -----------
# &   001 = 1

# 🟡 2. OR Operator |
# 👉 Rule: If any one is 1 → result is 1

# A	B	A | B
# 0	0	0
# 0	1	1
# 1	0	1
# 1	1	1

# 👉 Example:

# 5 = 101
# 3 = 011
# -----------
# |   111 = 7

# 🔵 3. XOR Operator ^ (VERY IMPORTANT)
# 👉 Rule: Same = 0, Different = 1

# A	B	A ^ B
# 0	0	0
# 0	1	1
# 1	0	1
# 1	1	0

# 👉 Example:

# 5 = 101
# 3 = 011
# -----------
# ^   110 = 6

# 👉 Key property:

# a ^ a = 0
# a ^ 0 = a

# 🔥 Used in:
# Single number
# Missing number
# Swapping


# 🔴 4. NOT Operator ~
# 👉 Rule: Flips all bits (0 → 1, 1 → 0)

# 👉 Example:

# 5 = 00000101
# ~5 = 11111010

# 👉 In most languages:

# ~n = -(n + 1)

# Example:
# ~5 = -6


# 🟣 5. Left Shift <<
# 👉 Rule: Shift bits left → multiply by 2

# n << k = n * (2^k)

# 👉 Example:

# 5 = 00000101
# 5 << 1 = 00001010 = 10
# 5 << 2 = 00010100 = 20


# 🟤 6. Right Shift >>
# 👉 Rule: Shift bits right → divide by 2

# n >> k = n / (2^k)

# 👉 Example:

# 5 = 00000101
# 5 >> 1 = 00000010 = 2

# ⚡ QUICK SUMMARY TABLE
# Operator	 Name	    Use
# &	         AND	   Check/set bits
# |	         OR	      Turn bits ON
# ^      	XOR	      Unique / toggle
# ~	        NOT	       Flip bits
# <<	   Left Shift	 Multiply by 2
# >>	   Right Shift	 Divide by 2

# 💡 INTERVIEW SHORT TRICKS
# 👉 Check even/odd:

# n & 1

# 👉 Remove last set bit:

# n & (n - 1)

# 👉 Get last set bit:

# n & (-n)

# 👉 Toggle ith bit:

# n ^ (1 << i)

# Interview Tip

# 👉 Always remember pattern:

# & → remove/check
# | → set
# ^ → toggle
# ~ → invert


#INTEGER TO BINARY
def int_to_binary(n):
    if n == 0:
        return "0"
    
    res = ""
    while n > 0:
        res = str(n % 2) + res
        n = n // 2

    return res

print(int_to_binary(10))   #1010
print(int_to_binary(2))    #10

print("___________")
#BINARY TO INTEGER
def binary_to_int(s):
    res = 0
    for i in s:
        res = res * 2 + int(i)
    return res

print(binary_to_int("1010"))  #10
print(binary_to_int("10"))   #2