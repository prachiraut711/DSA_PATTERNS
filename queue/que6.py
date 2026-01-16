# Generate Binary Representations from 1 to n
# Last Updated : 20 Sep, 2025
# Given an integer n, Generate the binary representations of all numbers from 1 to n.

# Examples: 

# Input: n = 4
# Output: [1, 10, 11, 100]
# Explanation:
# Binary representation of 1 → 1
# Binary representation of 2 → 10
# Binary representation of 3 → 11
# Binary representation of 4 → 100

# Input: n = 6
# Output: [1, 10, 11, 100, 101, 110]
# Explanation:
# Binary representation of 1 → 1
# Binary representation of 2 → 10
# Binary representation of 3 → 11
# Binary representation of 4 → 100
# Binary representation of 5 → 101
# Binary representation of 6 → 110


# 💡 Idea (Why Queue?)

# Binary numbers can be generated level by level, just like a tree:
# Start with "1"
# For every binary string:
# Append "0"
# Append "1"
# This is Breadth First Search (BFS) → naturally done using a queue.

from collections import deque
def generateBinary(n):
    result = []
    q = deque()

    q.append("1")
    for _ in range(n):
        curr = q.popleft()
        result.append(curr)

        q.append(curr + "0")
        q.append(curr + "1")
    
    return result

print(generateBinary(4))
print(generateBinary(6))

# If asked:

# “Why queue?”

# Say:

# “This is a BFS-style generation where each binary number produces the next two numbers by appending 0 and 1.”