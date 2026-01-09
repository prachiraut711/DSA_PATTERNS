
# 85. Maximal Rectangle  (extension of largest reactangle area)


# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

# Example 1:


# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
# Example 2:

# Input: matrix = [["0"]]
# Output: 0
# Example 3:

# Input: matrix = [["1"]]
# Output: 1
def maximalRectangle(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    col = len(matrix[0])
    heights = [0] * col
    maxArea = 0

    for r in range(rows):
        for c in range(col):
            if matrix[r][c] == "1":  #que madhe "1", "0",.. ase str madhe mag check kartana pn tasch "str" madge check kar nahitar error yeil
                heights[c] += 1
            else:
                heights[c] = 0
    
        maxArea = max(maxArea, largestRectangleArea(heights))
    return maxArea

def largestRectangleArea(heights):
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
                w = n - stack[-1] - 1
            else:
                w = n
            area = h * w
            maxArea = max(area, maxArea)

        return maxArea



print(maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(maximalRectangle([["0"]]))
print(maximalRectangle([["1"]]))

    