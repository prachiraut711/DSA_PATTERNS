# Problem: Swap Two Numbers Without Extra Space

# 👉 Question:

# Given two integers a and b,
# swap their values without using a third variable.

def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b

    return a, b

print(swap(2,3))
print(swap(5,10))

# Say this clearly:

# “I can swap using XOR without extra space”
# “XOR helps preserve values without loss”

# 👉 Also mention:

# a ^ a = 0
# a ^ 0 = a

# How it Works

# Initial:

# a = 5 (101)
# b = 3 (011)

# Step 1:

# a = a ^ b = 101 ^ 011 = 110 (6)

# Step 2:

# b = a ^ b = 110 ^ 011 = 101 (5)

# Step 3:

# a = a ^ b = 110 ^ 101 = 011 (3)

# 👉 Final:

# a = 3, b = 5