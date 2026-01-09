# 84. Largest Rectangle in Histogram

# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.


# Example 1:

# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Example 2:


# Input: heights = [2,4]
# Output: 4

def largestRectangle(heights):
    stack = []
    n = len(heights)
    maxArea = 0

    for i in range(n):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            if stack:
                w = i - stack[-1] - 1
            else:
                w = i
            area = h * w
            maxArea = max(maxArea, area)
        stack.append(i)

    while stack:
        h = heights[stack.pop()]
        if stack:
            w = n - stack[-1] -1
        else:
            w = n
        area = h * w
        maxArea = max(maxArea, area)
    
    return maxArea

print(largestRectangle([2,1,5,6,2,3]))
print(largestRectangle([2,4]))

 