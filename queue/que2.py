class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, x):
        new_node = Node(x)

        # If queue is empty
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

        # If queue becomes empty
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
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")
