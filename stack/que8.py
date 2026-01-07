# Next Greater Frequency Element
# Given an array, for each element find the value of the nearest element to the right which is having a frequency greater than that of the current element. If there does not exist an answer for a position, then make the value '-1'.
# Examples: 
# Input: arr[] = [2, 1, 1, 3, 2, 1]
# Output: [1, -1, -1, 2, 1, -1] 
# Explanation: 1 appears 3 times, 2 appears 2 times and 3 appears 1 time. 
# For arr[0] ie, 2 arr[1] ie 1 is the closest element on its right which has greater frequency than the frequency of 2. 
# For the arr[1] and arr[2] no element on the right has greater frequency than 1, so -1 will be printed. and so on. 

# Input: arr[] = [5, 1, 2, 3, 2, 5, 5, 4, 5, 2]
# Output: [-1, 2, 5, 2, 5, -1, -1, 5, -1, -1]

#right side ni vicharl mag right to left traverse kel and last la result la reverse kel same next greater from right sarkh just make dictionary to store frequencies and add freq[] in conditions.

# First, compute the frequency of every number in the array.
# Traverse the array from right to left, using a stack.
# Use the frequency instead of the value to determine which elements to keep in the stack.

from collections import Counter
def nextGreaterFrequencyElement(arr):
    stack = []
    res = []
    freq = Counter(arr)

    for i in range(len(arr) - 1, -1, -1):
        curr = arr[i]
        while stack and freq[stack[-1]] <= freq[curr]:
            stack.pop()
        if stack:
            res.append(stack[-1])
        else:
            res.append(-1)
        stack.append(curr)

    return res[::-1]

print(nextGreaterFrequencyElement([2, 1, 1, 3, 2, 1]))
print(nextGreaterFrequencyElement([5, 1, 2, 3, 2, 5, 5, 4, 5, 2]))
