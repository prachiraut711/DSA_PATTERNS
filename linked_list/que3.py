# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:
# Input: head = [1], n = 1
# Output: []
# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]
# Given a list like:
# Index from front:   1 → 2 → 3 → 4 → 5  
# Index from end:     5 ← 4 ← 3 ← 2 ← 1
# So:
# If n = 2, you remove 4 (the 2nd node from the end).
# If n = 1, you remove 5 (the last node).
# If n = 5, you remove 1 (the first node).

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
# mostly as jevva list print karychi asel delete karun tyatl kahi, tar return head karych
def removeNthFromEnd(head, n):
    slow = head
    fast = head

    for _ in range(n):
        fast = fast.next

    # Edge case: if fast is None, we are deleting the head
    if not fast:
        return head.next
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next
    return head  #head still points to the start of the modified list. jar slow pasun return kel ast tar ardhi ch list ali asti jithe last la,mahunu return head.
# mostly as jevva list print karychi asel delete karun tyatl kahi, tar return head karych

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

    ans = removeNthFromEnd(head, 2)
    print(printList(ans))

if __name__ == "__main__":
    main()

