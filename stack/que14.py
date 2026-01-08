
# 150. Evaluate Reverse Polish Notation
# Medium
# Topics
# premium lock icon
# Companies
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22


# In normal (infix) notation: 3 + 4
# In Reverse Polish Notation (postfix): 3 4 +
# Operator comes AFTER operands

# 🧠 Key Idea to Solve This Problem
# We use a stack.
# Rules:
# If token is a number → push it onto the stack
# If token is an operator (+ - * /) →
# Pop two numbers from stack
# Apply operation
# Push result back
# That’s it ✅

# truncate toward zero (SAFE)
# res = abs(a) // abs(b)
# if (a < 0) ^ (b < 0):
#     res = -res
# stack.append(res)

# but this is wrong for divison condition in 3rd example so the corrct leetcode accepted version is 
class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for i in tokens:
            if i in "+-*/":
                b = stack.pop()
                a = stack.pop()

                if i == "+":
                    stack.append(a + b)
                elif i == "-":
                    stack.append(a - b)
                elif i == "*":
                    stack.append(a * b)
                else:
                    # truncate toward zero (SAFE)
                    res = abs(a) // abs(b)
                    if (a < 0) ^ (b < 0):
                        res = -res
                    stack.append(res)
            else:
                stack.append(int(i))

        return stack[-1]



#this was correct for first 2 example but divison condition fail in 3rd example
def evalRPN(tokens):
    stack = []
    for i in tokens:
        if i in "+-*/":
            b = stack.pop()   #bottom la pahila el mag tyavar dusra jato stack madhe mag bottom ch a variable and op cha b variable
            a = stack.pop()
        
            if i == "+":
                stack.append(a + b)
            elif i == "-":
                stack.append(a - b)
            elif i == "*":
                stack.append(a * b)
            else:     #i == "/":
                stack.append(int(a / b))  #truncate(near) to zero as per rule mahnun int(a/b) kel mahnje fakt int val getli pudchi decimal value nahi getle pudche point chya
        
        else:     # i == number sel tar push in stack
            stack.append(int(i))   # as input in str format so while appending push in int form so while multiply and divison error will not happen
        
        return stack[-1]  #nust stack return kel tar ['2'] as list yetiye mag stack[-1] ni int value milel
    
print(evalRPN(["2","1","+","3","*"]))
print(evalRPN(["4","13","5","/","+"]))
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

# but this is wrong for divison condition in 3rd example so the corrct leetcode accepted version is 
class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for i in tokens:
            if i in "+-*/":
                b = stack.pop()
                a = stack.pop()

                if i == "+":
                    stack.append(a + b)
                elif i == "-":
                    stack.append(a - b)
                elif i == "*":
                    stack.append(a * b)
                else:
                    # truncate toward zero (SAFE)
                    res = abs(a) // abs(b)
                    if (a < 0) ^ (b < 0):
                        res = -res
                    stack.append(res)
            else:
                stack.append(int(i))

        return stack[-1]
