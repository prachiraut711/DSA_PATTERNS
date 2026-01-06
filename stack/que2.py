# Reverse a String using Stack
# Last Updated : 23 Jul, 2025
# Given a string str, the task is to reverse it using stack. 

# Example:

# Input: s = "GeeksQuiz"
# Output: ziuQskeeG

# Input: s = "abc"
# Output: cba


# 🚀 Algorithm (Step-by-Step)

# Create an empty stack

# Push every character of the string into the stack

# Pop characters one by one and add them to a result string

# Return the result
def reverse(s):
    stack = []

    for i in s:
        stack.append(i)
    
    res = ""
    while stack:
        res += stack.pop()
    return res

print(reverse("abc"))
print(reverse("GeeksQuiz"))