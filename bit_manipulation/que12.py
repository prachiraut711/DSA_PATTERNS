# Problem: Count Total Set Bits from 1 to N

# 👉 Given n, count total number of set bits (1s) in binary representation of all numbers from 1 to n.

# 🧪 Example
# n = 5

# Numbers:

# 1 → 001 → 1
# 2 → 010 → 1
# 3 → 011 → 2
# 4 → 100 → 1
# 5 → 101 → 2

# 👉 Total = 1 + 1 + 2 + 1 + 2 = 7

# ❌ Brute Force (Not for Interview)
# def countSetBits(n):
#     count = 0
#     for i in range(1, n+1):
#         count += bin(i).count('1')
#     return count

# ⛔ Time: O(n log n)

#approch 1 :Time Complexity: O(k*n), where k is the number of binary digits. Auxiliary Space: O(1).(but not that optimal)
def setBits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def countSetBits(n):
    res = 0
    for i in range(n + 1):
        res += setBits(i)
    return res

print(countSetBits(3))  #4
print(countSetBits(5))  #7
print("________")

#approch 2 -OPTIMAL APPROCH

#👉 Count bits position-wise instead of number-wise
# 💡 Key Idea
# For every bit position (0,1,2,3...):
# 👉 Pattern repeats every: 2^(i+1)
# 👉 In each cycle:
# Half bits = 1
# Half bits = 0
# 🟢 Formula Approach
# For each bit i:
# cycle = 2^(i+1)
# full_cycles = (n+1) // cycle
# bits_from_full = full_cycles * (cycle // 2)
# remaining = (n+1) % cycle
# extra_bits = max(0, remaining - (cycle // 2))

#see gfg page for this question
def countSetBits(n):
    count = 0
    i = 0

    while (1 << i) <= n:
        cycle = 1 << i + 1
        full_cycle = (n + 1) // cycle

        count += full_cycle * (cycle // 2)

        remainder = (n + 1) % cycle
        count += max(0, remainder - (cycle // 2))

        i += 1

    return count

print(countSetBits(3))  #4
print(countSetBits(5))  #7

# Intuition with Example (n = 5)
# Bit 0 (LSB)
# Pattern: 0 1 0 1 0 1 ...
# Count of 1s = 3
# Bit 1
# Pattern: 0 0 1 1 0 0 ...
# Count = 2
# Bit 2
# Pattern: 0 0 0 0 1 1 ...
# Count = 2

# 👉 Total = 3 + 2 + 2 = 7

# ⚡ Complexity
# Time: O(log n) ✅
# Space: O(1)
# 🔥 Interview Tips

# 👉 Say this clearly:

# “Instead of checking each number, I count bits position-wise”
# “Each bit follows a repeating pattern of size 2^(i+1)”

