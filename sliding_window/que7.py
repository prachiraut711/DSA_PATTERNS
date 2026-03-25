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