# 11. Container With Most Water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Example 1:

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1

def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        width = right - left    #horizontal axis varch distance width kadli by subtracting left from right
        h = min(height[left], height[right])  #height sathi ata min getl bcz max jar getl tar pani kali padel na ex 10 litre and 5 litre bucket the max water store wilbe 5 litre bucket bcz if fill with 10 litre then water will be fall
        area = width * h
        max_area = max(max_area, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
        
    return max_area

print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))













# Why width = right - left ?
# Think of the x-axis

# Each line is drawn at a position (index) on the x-axis

# Distance between two lines = difference of their indices

# index:   0     1     2     3
# lines:   |     |     |     |


# If we pick:

# left = 1
# right = 4


# 👉 The horizontal distance between them is:

# width = 4 - 1 = 3


# That is exactly how wide the container is.

# 📌 You cannot use:

# right + left ❌ (not distance)

# abs() ❌ (right is always > left)

# ❓ Why height = min(height[left], height[right]) ?
# Think about water in a container

# Water can only be filled up to the shortest wall.

# Visual idea:
# 8 |       |
#   |       |
#   |   7   |


# Even if one wall is taller:

# height[left] = 8
# height[right] = 7


# 👉 Water spills over the shorter wall (7)

# So effective water height = 7

# Real-life example

# Two buckets:

# One is 10 cm

# One is 5 cm

# Max water you can store = 5 cm

# ❌ Why not max(height[left], height[right]) ?

# If you use max:

# width = 7
# height = max(8,7) = 8
# area = 56 ❌ WRONG


# Because water cannot float above the shorter wall.

# ✅ Correct formula (must remember)
# area = (right - left) × min(height[left], height[right])