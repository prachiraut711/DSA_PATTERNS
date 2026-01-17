# It should support the following two operations: hit and getHits. hit(timestamp) – Shows a hit at the given timestamp. getHits(timestamp) –
# Returns the number of hits received in the past 5 minutes (300 seconds) (from currentTimestamp). 
# Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological 
# order (i.e. the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

# LeetCode – Design Hit Counter
# 📌 Problem Summary

# You need to design a system that records hits (events) at specific timestamps and can return how many hits happened in the past 5 minutes (300 seconds).

# Required Operations
# hit(timestamp)        → record a hit at given timestamp
# getHits(timestamp)    → return hits in last 300 seconds

# Important Constraints

# Timestamps are monotonically increasing (non-decreasing).

# Only hits in the range [timestamp - 299, timestamp] are counted.

# Both operations should be efficient.

# ✅ Best & Accepted Approach (Queue / Deque)

# We use a queue to store timestamps of hits.

# Why queue?

# Old hits must be removed from the front

# New hits are added at the back

# Order is guaranteed by timestamps

# 🧠 Core Idea

# Store every hit(timestamp) in a queue

# While calling getHits(timestamp):

# Remove timestamps < timestamp - 299

# Remaining queue size = answer

from collections import deque
class HitCounter(object):

    def __init__(self):
        self.q = deque()

    def hit(self, timestamp):
        self.q.append(timestamp)

    def getHits(self, timestamp):
        while self.q and self.q[0] <= timestamp - 299:
            self.q.popleft()
        
        return len(self.q)
    











