#implementation of circular queue  (“Circular queue uses modulo arithmetic to reuse empty spaces and avoid memory wastage.)
# 622. Design Circular Queue

# Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

# Implement the MyCircularQueue class:

# MyCircularQueue(k) Initializes the object with the size of the queue to be k.
# int Front() Gets the front item from the queue. If the queue is empty, return -1.
# int Rear() Gets the last item from the queue. If the queue is empty, return -1.
# boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
# boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
# boolean isEmpty() Checks whether the circular queue is empty or not.
# boolean isFull() Checks whether the circular queue is full or not.
# You must solve the problem without using the built-in queue data structure in your programming language. 

# 🔄 Circular Queue (Array Implementation)
# Why Circular Queue?

# Normal queue wastes space after dequeues.
# Circular queue reuses space by wrapping around using modulo %.

# ✅ Key Concepts

# front → index of first element

# rear → index of last element

# Queue is full when
# (rear + 1) % size == front

# Queue is empty when
# front == -1

class MyCircularQueue(object):

    def __init__(self, k):
        self.size = k
        self.queue = [None] * k
        self.front = -1
        self.rear = -1

    def enQueue(self, value):
        if self.isFull():
            return False
        
        if self.isEmpty():
            self.front = 0
        
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        
        return True
    
    def deQueue(self):
        if self.isEmpty():
            return False
        
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        
        return True
    
    def Front(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]
    
    def Rear(self):
        if self.isEmpty():
            return -1
        return self.queue[self.rear]
    
    def isFull(self):
        return (self.rear + 1) % self.size == self.front
    
    def isEmpty(self):
        return self.front == -1
    
    
cq = MyCircularQueue(3)

print(cq.enQueue(10))   # True
print(cq.enQueue(20))   # True
print(cq.enQueue(30))   # True
print(cq.enQueue(40))   # False

print(cq.Front())       # 10
print(cq.Rear())        # 30

print(cq.deQueue())     # True
print(cq.enQueue(40))   # True

print(cq.Rear())        # 40

