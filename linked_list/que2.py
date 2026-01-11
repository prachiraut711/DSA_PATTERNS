# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.
# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
# Example 1:
# Input: head = [1,3,4,7,1,2,6]
# Output: [1,3,4,1,2,6]
# Explanation:
# The above figure represents the given linked list. The indices of the nodes are written below.
# Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
# We return the new list after removing this node. 
# Example 2:
# Input: head = [1,2,3,4]
# Output: [1,2,4]
# Explanation:
# The above figure represents the given linked list.
# For n = 4, node 2 with value 3 is the middle node, which is marked in red.
# Example 3:
# Input: head = [2,1]
# Output: [2]
# Explanation:
# The above figure represents the given linked list.
# For n = 2, node 1 with value 1 is the middle node, which is marked in red.
# Node 0 with value 2 is the only node remaining after removing node 1.


#O(1) correct approch
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# mostly as jevva list print karychi asel delete karun tyatl kahi, tar return head karych
def deleteMid(head):
    if not head or head.next is None:  #some test case will be wrong idf not add this 
        return None
    
    prev = None
    slow = head
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next

    prev.next = slow.next  #prev comes before sloe this sequence is important

    return head  #head still points to the start of the modified list. jar prev return kel ast tar ardhi ch list ali asti jithe last la prev ahe thithun pn aplyala start pasun hav ,mahunu return head
# mostly as jevva list print karychi asel delete karun tyatl kahi, tar return head karych

def printList(head):
    result = []
    while head:
        result.append(head.data)  #append kartana nehmi append head.data karych nust head kel tar error yeil
        head = head.next
    return result


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next  = Node(3)
    head.next.next.next  = Node(4)

    head = deleteMid(head)
    print(printList(head))

if __name__ == "__main__":
    main()


#O(n) if not remeber above then
#O(n) approch
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

def getLength(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length

def deleteMid(head):
    length = getLength(head)

    if length == 1:
        return None
    
    middle_index = length // 2

    current = head
    for i in range(middle_index - 1):
        current = current.next
    current.next = current.next.next
    
    return head



