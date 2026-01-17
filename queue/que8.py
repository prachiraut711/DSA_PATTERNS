# 239. Sliding Window Maximum

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

#max ahe na que madhe mag monotonic decresing 
#it is MONOTONIC DECRESING QUEUE (top of queue < arr[i])
from collections import deque
def maxSlidingWindow(nums, k):
    if not nums or k == 0:
        return []
    
    dq = deque()
    res = []

    for i in range(len(nums)):
         # Step 1: remove indices out of window
        if dq and dq[0] <= i - k:
            dq.popleft()
        
         # Step 2: remove smaller elements
        while dq and nums[dq[-1]] <= nums[i]:   # SLIDING WINDOW MINIMUM QUE asel tar fakt ithe nums[dq[-1]] >= nums[i]   greater than eaual kar as its smaller so itwill be monotonic incresing queue
            dq.pop()
        # Step 3: add current index
        dq.append(i)
        
        # Step 4: record result
        if i >= k - 1:
            res.append(nums[dq[0]])
    
    return res

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(maxSlidingWindow([1], 1))
#*** SLIDING WINDOW MINIMUM QUE asel tar fakt ithe nums[dq[-1]] >= nums[i]   greater than eaual kar as its smaller so itwill be monotonic incresing queue


#dry run
# i = 0 → nums[0] = 1
# Deque before: []

# 1️⃣ Remove out-of-window?

# Deque empty → nothing happens

# 2️⃣ Remove smaller elements?

# Deque empty → nothing happens

# 3️⃣ Add index 0

# Deque = [0]   → values = [1]


# 4️⃣ Window formed?

# i < k-1 → NO output

# 🔹 i = 1 → nums[1] = 3
# Deque before: [0] → [1]

# 1️⃣ Remove out-of-window?

# i - k = -2

# 0 ≤ -2 ❌ → nothing removed

# 2️⃣ Remove smaller from back:

# nums[0] = 1 ≤ 3 ✅ → pop index 0

# Deque now empty

# 3️⃣ Add index 1

# Deque = [1] → [3]


# 4️⃣ Window formed?

# i < k-1 → NO output

# 🔹 i = 2 → nums[2] = -1
# Deque before: [1] → [3]

# 1️⃣ Remove out-of-window?

# i - k = -1

# 1 ≤ -1 ❌ → nothing removed

# 2️⃣ Remove smaller from back?

# nums[1] = 3 ≤ -1 ❌ → nothing removed

# 3️⃣ Add index 2

# Deque = [1, 2] → [3, -1]


# 4️⃣ Window formed?
# ✅ YES (i = 2)

# ➡️ Maximum = front of deque

# nums[1] = 3


# 📌 Result = [3]

# 🔹 i = 3 → nums[3] = -3
# Deque before: [1,2] → [3,-1]

# 1️⃣ Remove out-of-window?

# i - k = 0

# dq[0] = 1

# 1 ≤ 0 ❌ → nothing removed

# 2️⃣ Remove smaller from back?

# nums[2] = -1 ≤ -3 ❌ → nothing removed

# 3️⃣ Add index 3

# Deque = [1,2,3] → [3,-1,-3]


# 4️⃣ Window formed?
# ✅ YES

# ➡️ Max = nums[1] = 3

# 📌 Result = [3, 3]

# 🔹 i = 4 → nums[4] = 5
# Deque before: [1,2,3] → [3,-1,-3]

# 1️⃣ Remove out-of-window?

# i - k = 1

# dq[0] = 1

# 1 ≤ 1 ✅ → pop index 1

# Deque → [2,3]

# 2️⃣ Remove smaller from back:

# nums[3] = -3 ≤ 5 ✅ → pop

# nums[2] = -1 ≤ 5 ✅ → pop

# Deque empty now

# 3️⃣ Add index 4

# Deque = [4] → [5]


# 4️⃣ Window formed?
# ✅ YES

# ➡️ Max = nums[4] = 5

# 📌 Result = [3, 3, 5]

# 🔹 i = 5 → nums[5] = 3
# Deque before: [4] → [5]

# 1️⃣ Remove out-of-window?

# i - k = 2

# 4 ≤ 2 ❌ → nothing removed

# 2️⃣ Remove smaller?

# nums[4] = 5 ≤ 3 ❌ → nothing removed

# 3️⃣ Add index 5

# Deque = [4,5] → [5,3]


# 4️⃣ Window formed?
# ✅ YES

# ➡️ Max = nums[4] = 5

# 📌 Result = [3, 3, 5, 5]

# 🔹 i = 6 → nums[6] = 6
# Deque before: [4,5] → [5,3]

# 1️⃣ Remove out-of-window?

# i - k = 3

# 4 ≤ 3 ❌ → nothing removed

# 2️⃣ Remove smaller:

# nums[5] = 3 ≤ 6 ✅ → pop

# nums[4] = 5 ≤ 6 ✅ → pop

# Deque empty

# 3️⃣ Add index 6

# Deque = [6] → [6]


# 4️⃣ Window formed?
# ✅ YES

# ➡️ Max = 6

# 📌 Result = [3, 3, 5, 5, 6]

# 🔹 i = 7 → nums[7] = 7
# Deque before: [6] → [6]

# 1️⃣ Remove out-of-window?

# i - k = 4

# 6 ≤ 4 ❌

# 2️⃣ Remove smaller?

# nums[6] = 6 ≤ 7 ✅ → pop

# 3️⃣ Add index 7

# Deque = [7] → [7]


# 4️⃣ Window formed?
# ✅ YES

# ➡️ Max = 7

# 📌 Result = [3, 3, 5, 5, 6, 7]

# ✅ FINAL ANSWER
# [3, 3, 5, 5, 6, 7]

# 🧠 ONE SENTENCE TO REMEMBER

# We remove useless elements so the deque always keeps the maximum at the front.