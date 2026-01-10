# Given a singly linked list, the task is to find the middle of the linked list. If the number of nodes are even, then there would be two middle nodes, so return the second middle node.
# Example:
# Input: linked list: 1->2->3->4->5
# Output: 3 
# Explanation: There are 5 nodes in the linked list and there is one middle node whose value is 3.
# Input: linked list = 10 -> 20 -> 30 -> 40 -> 50 -> 60
# Output: 40
# Explanation: There are 6 nodes in the linked list, so we have two middle nodes: 30 and 40, but we will return the second middle node which is 40.

#to get middle
#correct approch
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def middleNode(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data  #return slow will give error return slow.data
    

def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)

    print(middleNode(head))

if __name__ == "__main__":
    main()



#for printing list from middle element
#leetcode question
# Middle of the Linked List
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


# Helper function to print list from a given node
def printList(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Example usage
if __name__ == "__main__":
    # Creating linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    sol = Solution()
    middle = sol.middleNode(head)

    print("Middle node and onwards:")
    print(printList(middle))


#This is O(n) approch
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getLength(head,):
    length = 0
    while head:
        length += 1
        head = head.next

    return length

def getMiddle(head):
    length = getLength(head)
    mid_index = length // 2
    while mid_index:
        head = head.next
        mid_index -= 1

    return head.data

def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)

    print(getMiddle(head))
   
if __name__ == "__main__":
    main()


        

