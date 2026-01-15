# Implement Stack using Queues(using 2 queues)

from collections import deque
class MyStack(object):

    def __init__(self):
        self.q = deque()
    
    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    
    def pop(self):
        return self.q.popleft()
    
    def top(self):
        return self.q[0]
    
    def empty(self):
        return len(self.q) == 0
    
s = MyStack()

s.push(1)
s.push(2)
s.push(3)

print(s.top())   # 3
print(s.pop())   # 3
print(s.top())   # 2
print(s.empty()) # False

    


# 1️⃣ __init__() – Constructor
# def __init__(self):
#     self.q = deque()

# What it does:

# Creates empty queue

# Initial state:
# Queue: []

# 2️⃣ push(x) – Push element into stack
# def push(self, x):
#     self.q.append(x)
#     for _ in range(len(self.q) - 1):
#         self.q.append(self.q.popleft())

# Goal:

# 👉 Make new element come to front (so it behaves like stack top)

# Example: push(10)
# append → [10]
# (no rotation)


# Queue:

# [10]

# Example: push(20)

# 1️⃣ Append:

# [10, 20]


# 2️⃣ Rotate once:

# popleft → 10
# append → [20, 10]


# Queue:

# [20, 10]

# Example: push(30)

# 1️⃣ Append:

# [20, 10, 30]


# 2️⃣ Rotate twice:

# popleft 20 → [10, 30, 20]
# popleft 10 → [30, 20, 10]


# Queue:

# [30, 20, 10]


# ✔ Front is always stack top

# 3️⃣ pop() – Remove top element
# def pop(self):
#     return self.q.popleft()

# Why this works:

# Front of queue is top of stack

# Example:
# Queue: [30, 20, 10]


# pop() removes:

# 30


# Queue becomes:

# [20, 10]

# 4️⃣ top() – Get top element
# def top(self):
#     return self.q[0]

# Example:
# Queue: [20, 10]


# top() returns:

# 20


# (No removal)

# 5️⃣ empty() – Check if stack is empty
# def empty(self):
#     return len(self.q) == 0

# Example:
# Queue: []


# Returns:

# True


# If:

# Queue: [10]


# Returns:

# False