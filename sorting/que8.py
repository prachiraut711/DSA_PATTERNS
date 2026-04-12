# Top K Frequent Elements ⭐
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2

# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1

# Output: [1]

# Example 3:

# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

# Output: [1,2]
# (LeetCode 347)

# ✅ Problem

# Return k most frequent elements

# 🧠 Approach (Heap)
# Count frequency (HashMap)
# Use min heap of size k

# Problem

# Input:

# nums = [1,1,1,2,2,3]
# k = 2

# 👉 Output:

# [1, 2]   (because 1 appears 3 times, 2 appears 2 times)
# 🔹 Step 1: Count Frequency (VERY IMPORTANT)
# from collections import Counter

# count = Counter(nums)
# print(count)

# 👉 Output:

# {1: 3, 2: 2, 3: 1}

# Meaning:

# 1 → 3 times
# 2 → 2 times
# 3 → 1 time
# 🔹 Step 2: Why Heap?

# We only need top k = 2 elements, not all.

# 👉 So we use a min heap of size k

# smallest frequency stays on top
# if size > k → remove smallest
# 🔹 Step 3: Dry Run (IMPORTANT)

# We push (frequency, number) into heap.

# ➤ Start with empty heap
# heap = []
# ➤ Insert (3,1)
# heap = [(3,1)]
# ➤ Insert (2,2)
# heap = [(2,2), (3,1)]

# (heap automatically sorts by first value → frequency)

# ➤ Insert (1,3)
# heap = [(1,3), (3,1), (2,2)]

# ⚠️ Now size = 3 > k (2)

# 👉 Remove smallest:

# pop → (1,3)

# Now:

# heap = [(2,2), (3,1)]
# 🔹 Step 4: Extract Answer

# Heap contains:

# [(2,2), (3,1)]

# We only need numbers:

# [2, 1]

# Order doesn't matter ✅

from collections import Counter
import heapq

def topKFrequent(nums, k):
    count = Counter(nums)
    heap = []

    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)

    result = []
    for freq, num in heap:
        result.append(num)
    return result

#or here  - return [num for freq, num in heap] i nstead the result var
print(topKFrequent([1,1,1,2,2,3], 2))   #[1,2]
print(topKFrequent([1,1,1,1,2,3,3,3, 5,5], 3)) #[1,3,5]

# ⚡ When to Use This Pattern
# Use this when:
# "Top K"
# "K largest/smallest"
# "Most frequent"
