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
