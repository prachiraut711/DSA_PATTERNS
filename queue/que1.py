# Implement Queue using Array

# What is a Queue?
# A Queue follows FIFO (First In, First Out)
# Operations:
# enqueue(x) → insert element
# dequeue() → remove element
# front() → peek front
# isEmpty()

class queue:
    def __init__(self):
        self.arr = []
        self.front_index = 0

    def enqueue(self, x):
        self.arr.append(x)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        val = self.arr[self.front_index]
        self.front_index += 1
        return val
    
    def front(self):
        if self.isEmpty():
            return None
        return self.arr[self.front_index]
    
    def isEmpty(self):
        return self.front_index == len(self.arr)


q = queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.arr[q.front_index : ])  #[10, 20, 30]
print(q.dequeue())  #10
print(q.isEmpty())  #False
print(q.front())   #20
print(q.dequeue())  #20
print(q.front())   #30
print(q.dequeue()) #30
print(q.front())   #None
print(q.isEmpty())  #True


# 🔹 Key Idea of This Queue

# Instead of removing elements from the array (which is costly), we:

# Keep all elements in the array

# Move a pointer called front_index

# Elements before front_index are considered deleted

# So:

# enqueue → append

# dequeue → move front_index

# 📦 Initial State
# q = Queue()


# Internal values:

# arr = []
# front_index = 0


# Queue is empty because:

# front_index == len(arr) → 0 == 0 ✅

# ➕ enqueue(10)
# q.enqueue(10)


# What happens:

# self.arr.append(10)


# State:

# arr = [10]
# front_index = 0


# Queue content (logical):

# [10]
#  ↑
# front

# ➕ enqueue(20)
# q.enqueue(20)


# State:

# arr = [10, 20]
# front_index = 0


# Queue:

# [10, 20]
#  ↑
# front

# ➕ enqueue(30)
# q.enqueue(30)


# State:

# arr = [10, 20, 30]
# front_index = 0


# Queue:

# [10, 20, 30]
#  ↑
# front

# ❌ dequeue()
# q.dequeue()

# Step-by-step:
# val = self.arr[self.front_index]  # arr[0] = 10
# self.front_index += 1


# State after dequeue:

# arr = [10, 20, 30]
# front_index = 1


# Returned value:

# 10


# Logical queue now:

# [20, 30]
#      ↑
#    front


# ⚠️ 10 is not removed from array, but we ignore it.

# ❌ dequeue() again
# q.dequeue()

# val = arr[1] → 20
# front_index = 2


# State:

# arr = [10, 20, 30]
# front_index = 2


# Logical queue:

# [30]
#   ↑
# front

# 👀 front()
# q.front()

# return arr[front_index] → arr[2] → 30


# ✔ Correct front element

# ❌ dequeue() again
# q.dequeue()


# State:

# arr = [10, 20, 30]
# front_index = 3


# Logical queue:

# (empty)

# ❓ isEmpty()
# q.isEmpty()


# Check:

# front_index == len(arr)
# 3 == 3 → True


# ✔ Queue is empty

# 🧠 Why This Works Efficiently
# Operation	Time
# enqueue	O(1)
# dequeue	O(1)
# front	O(1)

# We never shift elements, only move front_index.

# ⚠️ One Small Drawback

# Array keeps old values:

# [10, 20, 30]


# But they are ignored.

# 👉 In long-running systems, we may:

# Periodically clean the array

# Or use Circular Queue

# 🗣 Interview Explanation (Say This)

# “Instead of removing elements from the array, we maintain a front index. Dequeue just moves the pointer, making operations O(1).”