# Implement Queue using Two Stacks  (using 2 stacks)

class MyQueue(object):
# We use two stacks:
# in_stack → for inserting elements
# out_stack → for removing / viewing elements

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]
    
    def pop(self):
        self.peek()
        return self.out_stack.pop()
    
    def isEmpty(self):
        return not self.in_stack and not self.out_stack
    

q = MyQueue()

q.push(1)
q.push(2)
q.push(3)

print(q.peek())  # 1
print(q.pop())   # 1
print(q.peek())  # 2
print(q.isEmpty()) # False



# Example:
# q.push(10)
# q.push(20)
# q.push(30)

# State after pushes:
# in_stack  = [10, 20, 30]
# out_stack = []


# ✔ Push is always O(1)

# Example:
# q.peek()

# Step-by-step transfer:
# pop 30 → out_stack = [30]
# pop 20 → out_stack = [30, 20]
# pop 10 → out_stack = [30, 20, 10]


# Now:

# in_stack  = []
# out_stack = [30, 20, 10]

# Front of queue:
# out_stack[-1] = 10


# ✅ peek() returns 10

# Example:
# q.pop()


# Before pop:

# out_stack = [30, 20, 10]


# After pop:

# out_stack = [30, 20]


# ✅ Removed element → 10

# Example:
# q.empty()


# If:

# in_stack  = []
# out_stack = []


# ➡ Returns True

# Else:
# ➡ Returns False