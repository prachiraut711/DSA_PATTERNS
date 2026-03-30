# Two odd Occuring
# Given an unsorted array, arr[] of positive numbers that contains even number of occurrences for all numbers except two numbers. Return that two numbers in decreasing order which has odd occurrences.

# Examples:

# Input: arr = [4, 2, 4, 5, 2, 3, 3, 1]
# Output: [5, 1] 
# Explanation: 5 and 1 have odd occurrences.
# Input: arr[] = [1, 7, 5, 7, 5, 4, 7, 4]
# Output: [7, 1]
# Explanation: 7 and 1 have odd occurrences.

# 👉 In an array:

# Exactly 2 numbers appear odd number of times
# All others appear even times
# 👉 Find those 2 numbers
# 🧠 Core Idea (VERY IMPORTANT)

# 👉 Use XOR:

# Step 1:

# XOR all elements → you get:

# xor = x ^ y

# (where x and y are the two odd occurring numbers)

# Step 2:

# Find a set bit in xor (where x and y differ)

# 👉 Use:

# set_bit = xor & -xor
# Step 3:

# Divide numbers into 2 groups:

# Group 1 → bit is set
# Group 2 → bit is NOT set

# 👉 Then XOR separately → you get both numbers

# 🔍 DETAILED EXAMPLE
# Input:
# arr = [1, 2, 3, 2, 3, 1, 4, 5]

# 👉 Frequencies:

# 1 → 2 times
# 2 → 2 times
# 3 → 2 times
# 4 → 1 time ✅
# 5 → 1 time ✅

# 👉 Answer should be: 4 and 5

# 🔶 STEP 1: XOR All Elements
# 1 ^ 2 ^ 3 ^ 2 ^ 3 ^ 1 ^ 4 ^ 5

# Cancel pairs:

# (1 ^ 1) = 0  
# (2 ^ 2) = 0  
# (3 ^ 3) = 0  

# Left:

# 0 ^ 0 ^ 0 ^ 4 ^ 5 = 4 ^ 5

# 👉 So:

# xor = 4 ^ 5
# Binary:
# 4 = 100
# 5 = 101
# -----------
# xor = 001
# 🔶 STEP 2: Find Rightmost Set Bit
# set_bit = xor & -xor
# xor = 001
# -xor = 111 (2's complement)
# ------------
# &   = 001

# 👉 So set_bit = 1 (last bit)

# 🔶 STEP 3: Divide into Groups

# 👉 Based on last bit:

# Group 1 (bit = 1):
# 1, 3, 3, 1, 5
# Group 2 (bit = 0):
# 2, 2, 4
# 🔶 STEP 4: XOR Each Group
# Group 1:
# 1 ^ 3 ^ 3 ^ 1 ^ 5
# = (1^1) ^ (3^3) ^ 5
# = 0 ^ 0 ^ 5 = 5
# Group 2:
# 2 ^ 2 ^ 4
# = (2^2) ^ 4
# = 0 ^ 4 = 4
# 🎯 FINAL ANSWER
# 4 and 5

def two_odd_number(arr):
    xor = 0
    
    # Step 1: XOR all
    for num in arr:
        xor ^= num
    
    # Step 2: find set bit
    set_bit = xor & -xor
    
    x = 0
    y = 0
    
    # Step 3: divide and XOR
    for num in arr:
        if num & set_bit:
            x ^= num
        else:
            y ^= num
    
    return x, y

#for gfg question  return max(x, y), min(x, y)  bcz GFG expects descending order

print(two_odd_number([1, 2, 3, 2, 3, 1, 4, 5]))  #4,5
print(two_odd_number([4, 2, 4, 5, 2, 3, 3, 1]))  #5,1
    
    
# Key Concepts to SAY in Interview

# 👉 “XOR cancels even occurrences”
# 👉 “Remaining XOR = x ^ y”
# 👉 “Use rightmost set bit to split into two groups”