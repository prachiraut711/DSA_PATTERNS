# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
# Example 1:
# Input: head = [1,2,2,1]
# Output: true
# Example 2:
# Input: head = [1,2]
# Output: false

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def isPalindrome(head):

    def reverseList(head):
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    
# We use Node(...) in copyList because a linked list is made of nodes, not just values.
# If you don’t create new Node objects, you are not copying the list, you are reusing the same nodes.
    def copyList(head):
        if not head:   #this is IMP for test case =[1]
            return None
        
        new_head = Node(head.data)
        old_node = head.next
        new_node = new_head

        while old_node:
            new_node.next = Node(old_node.data)
            old_node = old_node.next
            new_node = new_node.next
        return new_head
    
    def isEqual(l1, l2):
        while l1 and l2:
            if l1.data != l2.data:
                return False
            l1 = l1.next
            l2 = l2.next
        return True
    
    copied_list = copyList(head)
    reverse_list = reverseList(copied_list)  #reverse kel copy list not original list
    return isEqual(head, reverse_list)  #compare kel head means original list with reversed_list ithe copied list barobar nahi kel compare because aplyala original barobar karych ahe .ithe copy list banvli so we get reverse list of that copy list

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(1)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)

    
    print(isPalindrome(head))   #isPalindrome is defined inside your Solution 

if __name__ == "__main__":
    main()
