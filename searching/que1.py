# Linear Search

# Linear search is the simplest searching algorithm. It sequentially checks each element of the list until it finds the target value.

# Steps:
# Start from the first element of the list.
# Compare each element of the list with the target value.
# If the element matches the target value, return its index.
# If the target value is not found after iterating through the entire list, return -1.

# Idea

# Check each element one by one until you find the target.

# 🧠 Approach
# Start from index 0
# Compare each element with target
# If found → return index
# Else → return -1
# ⏱ Complexity
# Time: O(n)
# Space: O(1)

#que is to return index of target element in array.
def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linearSearch([4, 2, 7, 1, 9], 7)) #2
print(linearSearch([8, 6, 7, 2, 9], 10))  #-1