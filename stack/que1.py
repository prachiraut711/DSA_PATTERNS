# 20. Valid Parentheses
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

def isValid(s):
    stack = []
    pairs= {"}": "{", ")" : "(", "]" : "["}

    for i in s:
        if i in pairs.values():
            stack.append(i)
        elif i in pairs:
            if not stack or stack[-1] != pairs[i]:  ##or not and stack not empty or if top is not equal to open bracket
                return False
            stack.pop()
    return not stack
    
print(isValid("{((()}))"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([])"))
print(isValid("([)]"))