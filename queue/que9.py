# 933. Number of Recent Calls

# You have a RecentCounter class which counts the number of recent requests within a certain time frame.

# Implement the RecentCounter class:

# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.


# Example 1:

# Input
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# Output
# [null, 1, 2, 3, 3]

# Explanation
# RecentCounter recentCounter = new RecentCounter();
# recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
# recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
# recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
# recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
 

# Constraints:

# 1 <= t <= 109
# Each test case will call ping with strictly increasing values of t.
# At most 104 calls will be made to ping.


# What the question is ABOUT (Plain English)

# Imagine you are building a server or website that receives requests (pings).

# Every time a request comes in at time t (in milliseconds), you want to know:

# How many requests happened in the last 3000 milliseconds, including now?

# That’s it.
# No math tricks, no arrays initially — just count recent requests.

from collections import deque
class RecentCounter(object):

    def __init__(self):
        self.q = deque()

    def ping(self, t):
        self.q.append(t)
        
        # Remove old pings
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
        
        return len(self.q)
    
# 🔹 What does “recent” mean?

# If the current ping time is t, then:

# Recent calls = calls with time in range [t - 3000, t]


# ✅ Include t
# ❌ Exclude anything older than t - 3000

# 🔹 What does the class do?

# You need to implement this class:

# RecentCounter()
# ping(t)

# 1️⃣ RecentCounter()

# Creates a new counter

# Initially no calls

# 2️⃣ ping(t)

# A request comes at time t

# You must:

# Store this call

# Remove calls that are too old

# Return how many calls are recent

# 🔹 Important Given Rules

# ping(t) calls come in increasing order of t

# Time is in milliseconds

# You don’t need to sort anything

# 🔹 Example Explained Slowly
# Input:
# ping(1)
# ping(100)
# ping(3001)
# ping(3002)

# ping(1)

# Recent window: [-2999, 1]

# Calls so far: [1]

# ✅ Count = 1

# ping(100)

# Recent window: [-2900, 100]

# Calls so far: [1, 100]

# ✅ Count = 2

# ping(3001)

# Recent window: [1, 3001]

# Calls so far: [1, 100, 3001]

# All are valid

# ✅ Count = 3

# ping(3002)

# Recent window: [2, 3002]

# Calls so far: [1, 100, 3001, 3002]

# ❌ 1 is too old → remove it

# Remaining: [100, 3001, 3002]

# ✅ Count = 3

# 🔹 What problem type is this?

# This is a Sliding Window problem.

# Window size = 3000 ms

# Window moves forward with each ping

# 🔹 Why Queue is Perfect Here?

# Because:

# Calls come in order

# Old calls must be removed from the front

# New calls added to the back

# 👉 Exactly what a queue does.

# 🔹 What the question is NOT asking

# ❌ Not asking for max / min
# ❌ Not asking for sorting
# ❌ Not asking for binary search
# ❌ Not asking for timestamps difference pairs

# 🎯 One-Line Interview Explanation

# “Each ping records a timestamp, and we return how many timestamps fall within the last 3000 milliseconds using a sliding window.”

