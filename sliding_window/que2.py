# First negative in every window of size k
# Difficulty: MediumAccuracy: 48.61%Submissions: 217K+Points: 4Average Time: 15m
# Given an array arr[]  and a positive integer k, find the first negative integer for each and every window(contiguous subarray) of size k.

# Note: If a window does not contain a negative integer, then return 0 for that window.

# Examples:

# Input: arr[] = [-8, 2, 3, -6, 10] , k = 2
# Output: [-8, 0, -6, -6]
# Explanation:
# Window [-8, 2] First negative integer is -8.
# Window [2, 3] No negative integers, output is 0.
# Window [3, -6] First negative integer is -6.
# Window [-6, 10] First negative integer is -6.
# Input: arr[] = [12, -1, -7, 8, -15, 30, 16, 28] , k = 3
# Output: [-1, -1, -7, -15, -15, 0] 
# Explanation:
# Window [12, -1, -7] First negative integer is -1.
# Window [-1, -7, 8] First negative integer is -1.
# Window [-7, 8, -15] First negative integer is -7.
# Window [8, -15, 30] First negative integer is -15.
# Window [-15, 30, 16] First negative integer is -15.
# Window [30, 16, 28] No negative integers, output is 0.
# Input: arr[] = [12, 1, 3, 5] , k = 3
# Output: [0, 0] 
# Explanation:
# Window [12, 1, 3] No negative integers, output is 0.
# Window [1, 3, 5] No negative integers, output is 0.

# Constraints:
# 1 <= arr.size() <= 106
# -105 <= arr[i] <= 105
# 1 <= k <= arr.size()

# What the question wants

# You are given:

# An array arr

# A window size k

# For every contiguous subarray (window) of size k, you must:

# Find the first negative number in that window

# If there is no negative number, output 0

# ❌ Brute Force (Why it’s not good)

# For every window, scan all k elements → O(n × k)
# With n up to 10⁶, this will TLE ❌

# So we need an O(n) solution.

# ✅ Optimal Approach (Sliding Window + Queue)
# 💡 Key Idea

# Maintain a queue that stores indices of negative numbers in the current window

# The front of the queue always gives the first negative in the window

# 🧠 Algorithm (Step-by-Step)

# Create an empty queue q

# Traverse array using index i

# If arr[i] < 0, push index i into q

# Once window size reaches k:

# Remove elements from q that are outside the window

# If q is empty → answer is 0

# Else → answer is arr[q[0]]

from collections import deque
def firstNegative(arr, k):
    q = deque()      # stores indices of negative numbers
    result = []

    for i in range(len(arr)):
        # Step 1: Add current element if it is negative
        if arr[i] < 0:
            q.append(i)

        # Step 2: When window size reaches k
        if i >= k - 1:
            # Remove elements out of current window
            while q and q[0] < i - k + 1:
                q.popleft()

            # Step 3: Get answer for current window
            if q:
                result.append(arr[q[0]])
            else:
                result.append(0)
    return result

print(firstNegative([-8, 2, 3, -6, 10], 2))
print(firstNegative([12, -1, -7, 8, -15, 30, 16, 28], 3))
print(firstNegative([4,4,4], 3))

