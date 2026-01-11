# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:
# Input: head = [1,2]
# Output: [2,1]
# Example 3:
# Input: head = []
# Output: []

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseList(head):
    prev = None
    curr = head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    return prev

def printList(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    return result

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    reverse_list = reverseList(head)
    print(printList(reverse_list))

if __name__ == "__main__":
    main()
