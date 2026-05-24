# 8) Contains Duplicate

# (LeetCode 217)

# Question

# Check whether array contains duplicate elements.

# Example:

# arr = [1,2,3,1]

# Output:

# True
# Algorithm
# Create set/hashmap.
# Traverse array.
# If element already exists:
# return True
# Else store it.
# If traversal completes:
# return False


def isDuplicate(arr):
    freq = {}
    for num in arr:
        if num in freq:
            return True
        else:
            freq[num] = 1

    return False

print(isDuplicate([1,2,3,1]))  #true
print(isDuplicate([1,2,3,4]))  #false
