# https://www.geeksforgeeks.org/dsa/delete-middle-element-stack/
# Delete middle element of a stack
# Given a stack with push(), pop(), and empty() operations, The task is to delete the middle element of it without using any additional data structure.

# Input: s = [10, 20, 30, 40, 50]
# Output: [50, 40, 20, 10]
# Explanation: The bottom-most element will be 10 and the top-most element will be 50. Middle element will be element at index 3 from bottom, which is 30. Deleting 30, stack will look like [10, 20, 40, 50].

# Input: s = [5, 8, 6, 7, 6, 6, 5, 10, 12, 9]
# Output: [9, 12, 10, 5, 6, 7, 6, 8, 5]


#Interview-Expected Approach (Using Recursion)
def deleteMid(s):
    n = len(s)
    mid = n // 2

    def helper(i):
        if not s:
            return

        temp = s.pop()
        helper(i + 1)

        # skip correct middle element
        if i != mid:
            s.append(temp)

    helper(0)
    return s
print(deleteMid([10, 20, 30, 40, 50]))
print(deleteMid([5, 8, 6, 7, 6, 6, 5, 10, 12, 9]))


# return-------means Backtracking (Rebuilding stack in reverse)

# ⚠️ Why the stack is reversed?
# Because:
# We popped elements from top to bottom
# We pushed them back during backtracking
# This naturally reverses the order


#i cant use this as question sy--The task is to delete the middle element of it WITHOUT using any additional data structure.
def deleteMid(s):
    stack = []

    while s:
        stack.append(s.pop())

    mid = len(stack) // 2    #len(s)//2 kel tar wrong as yety

    stack.pop(mid)

    return stack
# 🚫 Uses an extra stack (stack) → not allowed

# 🚫 Changes the order of elements

# 🚫 Returns a list, not the original stack structure

print(deleteMid([10, 20, 30, 40, 50]))
print(deleteMid([5, 8, 6, 7, 6, 6, 5, 10, 12, 9]))