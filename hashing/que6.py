# 6) First Repeating Element
# Question

# Find first element that repeats in array.

# Example:

# arr = [2,5,1,2,3,5]

# Output:

# 2

# Algorithm

# Create hashmap.
# Traverse array.
# If element already exists:
# return that element
# Else store it.


def firstRepeatingEl(arr):
    freq = {}
    for num in arr:
        if num in freq:
            return num
        else:
            freq[num] = 1
    
    return -1

print(firstRepeatingEl([2,5,1,2,3,5]))  #2
print(firstRepeatingEl([1,2,3,4]))  #-1