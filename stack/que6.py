# Next Greater Element (NGE) for every element in given Array
# Given an array arr[] of integers, the task is to find the Next Greater Element for each element of the array in order of their appearance in the array.
# Note: The Next Greater Element for an element x is the first greater element on the right side of x in the array. Elements for which no greater element exist, consider the next greater element as -1. 

# Examples: 
# Input: arr[] = [1, 3, 2, 4]
# Output: [3, 4, 4, -1]
# Explanation: The next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4, since it doesn't exist, it is -1.

# Input: arr[] = [6, 8, 0, 1, 3]
# Output: [8, -1, 1, 3, -1]
# Explanation: The next larger element to 6 is 8, for 8 there is no larger elements hence it is -1, for 0 it is 1 , for 1 it is 3 and then for 3 there is no larger element on right and hence -1.

# Input: arr[] = [50, 40, 30, 10]
# Output: [-1, -1, -1, -1]
# Explanation: There is no greater element for any of the elements in the array, so all are -1.

#(QUE MADHE RIGHT SIDE CH VICHARL MAG RIGHT TO LEFT TRAVERSE KEL AND LAST LA RESULT LA REVERSE KEL)

# Initialize empty stack and empty result list.
# Traverse the array from right to left.
# For each element arr[i]:
# While the stack is not empty and the top of the stack ≤ current element, pop it.
# If the stack is not empty, then stack[-1] is the Next Greater Element.
# Else, no greater element → add -1.
# Push arr[i] to the stack.
# At the end, reverse the result list because we built it from right to left.

# # this is MONTONIC DECRESING STACK EXAMPLE
#(QUE MADHE RIGHT SIDE CH VICHARL MAG RIGHT TO LEFT TRAVERSE KEL AND LAST LA RESULT LA REVERSE KEL)
def nextGreaterElements(nums):
    stack = []
    result = []

    for i in range(len(nums) -1 ,-1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)
        stack.append(nums[i])

    return result[::-1]

print(nextGreaterElements([6, 8, 0, 1, 3]))
print(nextGreaterElements([50, 40, 30, 10]))

