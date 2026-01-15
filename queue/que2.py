#Implement Queue using Linked List

# 🔹 Basic Idea (Queue using Linked List)

# Queue follows FIFO (First In First Out)

# Enqueue → insert at rear

# Dequeue → remove from front

# We maintain two pointers:

# front → first element

# rear → last element

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, x):
        new_node = Node(x)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.data
    
    def peek(self):
        if self.front is None:
            return None
        return self.front.data
    
    def isEmpty(self):
        return self.front is None
    
    def display(self):
        curr = self.front
        while curr:
            print(curr.data, end="->")
            curr = curr.next
        print("None")


q = queue()
print(q.isEmpty()) #True
q.enqueue(10)
print(q.isEmpty())#false
q.enqueue(20)
q.enqueue(30)
q.display()   #10->20->30->None
print(q.dequeue())  #10
print(q.peek())  #20
q.display()   #20->30->None




# Example: enqueue(10)

# Queue is empty → both front and rear point to new node

# front → 10 → None
# rear  → 10

# Example: enqueue(20)
# rear.next = new_node
# rear = new_node


# Result:

# front → 10 → 20 → None
# rear


# Example: dequeue()

# Before:

# front → 10 → 20 → None
# rear            ↑


# Remove front (10):

# After:

# front → 20 → None
# rear  → 20


# Returned value → 10

# Dequeue last element
# front → 20 → None
# rear  → 20


# After dequeue:

# front = None
# rear  = None


# Queue becomes empty ✅

# Queue: 10 → 20 → 30
# peek() → 10

# If front is None, queue is empty.

# 10 -> 20 -> 30 -> None
