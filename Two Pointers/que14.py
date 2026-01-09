#https://leetcode.com/problems/trapping-rain-water/
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9


# At any index i, the water trapped is:
# water[i] = min(max height on left, max height on right) - height[i]
# So:
# You need a taller bar on both sides

def trap(height):
    left = 0
    right = len(height) - 1
    leftMax = 0
    rightMax = 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= leftMax:
                leftMax = height[left]
            else:
                water += leftMax - height[left]
            left += 1
        else:
            if height[right] >= rightMax:
                rightMax = height[right]
            else:
                water += rightMax - height[right]
            right -= 1
    return water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))


#same logic but littele simple
#def trap(height):
    # n = len(height)
    # leftMax = [0]*n
    # rightMax = [0]*n

    # leftMax[0] = height[0]
    # for i in range(1, n):
    #     leftMax[i] = max(leftMax[i-1], height[i])

    # rightMax[n-1] = height[n-1]
    # for i in range(n-2, -1, -1):
    #     rightMax[i] = max(rightMax[i+1], height[i])

    # water = 0
    # for i in range(n):
    #     water += min(leftMax[i], rightMax[i]) - height[i]

    # return water
