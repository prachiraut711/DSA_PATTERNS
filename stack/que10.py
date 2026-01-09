# Next Smaller Element   (on RIGHT SIDE in an array)
# Last Updated : 06 Jun, 2025
# Given an array, print the Next Smaller Element (NSE) for every element. The NSE for an element x is the first smaller element on the right side of x in the array. For elements for which no smaller element exists (on the right side), then consider NSE as -1. 
# Examples:
# Input: [4, 8, 5, 2, 25]
# Output: [2, 5, 2, -1, -1]
# Explanation: 
# The first element smaller than 4 having index > 0 is 2.
# The first element smaller than 8 having index > 1 is 5.
# The first element smaller than 5 having index > 2 is 2.
# There are no elements smaller than 4 having index > 3.
# There are no elements smaller than 4 having index > 4.

# Input: [13, 7, 6, 12]
# Output: [7, 6, -1, -1]
# Explanation: 
# The first element smaller than 13 having index > 0 is 7.
# The first element smaller than 7 having index > 1 is 6.
# There are no elements smaller than 6 having index > 2.
# There are no elements smaller than 12 having index > 3. 


# Start from the end of array (right to left).
# For each element:
# Pop stack elements that are greater than or equal to current element (since they can't be NSE).
# If the stack is not empty, the top of the stack is the next smaller.
# If stack is empty, NSE is -1.
# Push current element to stack.


#if asked from RIGHT SIDE THE TRAVERSE FROM RIGHT TO LEFT AND INLAST REVERSE THE RESULT 
#yat que madhe left side che smaller vvicharlet mag left side la tar right to left reverse ,fakt stack cha top > ahe ka te bagych element peksha smaller la
#this is MONOTONIC INCREASING STACK  problem(means stack's top > element)
def nextSmallerElement(arr):
    stack = []
    res = []

    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        if stack:
            res.append(stack[-1])
        else:
            res.append(-1)
        stack.append(arr[i])
        
    return res[::-1]

print(nextSmallerElement([4, 8, 5, 2, 25]))
print(nextSmallerElement([13, 7, 6, 12]))
