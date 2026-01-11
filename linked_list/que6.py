# There is a singly-linked list head and we want to delete a node node in it.
# You are given the node to be deleted node. You will not be given access to the first node of head.
# All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.
# Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:
# The value of the given node should not exist in the linked list.
# The number of nodes in the linked list should decrease by one.
# All the values before node should be in the same order.
# All the values after node should be in the same order.
# Custom testing:
# For the input, you should provide the entire linked list head and the node to be given node. node should not be the last node of the list and should be an actual node in the list.
# We will build the linked list and pass the node to your function.
# The output will be the entire list after calling your function.
# Example 1:
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
# Example 2:
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next  #not return anything BCZ  You're not creating a new list or returning a modified list — you're just mutating the existing list structu


def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def main():
    head = ListNode(4)
    head.next = ListNode(5)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)
    
    node_to_delete = head.next  # Node with value 5

    # Correct method call using instance of Solution
    Solution().deleteNode(node_to_delete)

    print(print_list(head))  # Output: [4, 1, 9]


if __name__ == "__main__":
    main()


# Step 1️⃣ Copy next node’s value into current node
# node.val = node.next.val


# Before:

# 4 → 5 → 1 → 9


# After copying:

# 4 → 1 → 1 → 9
#       ↑
#    current node