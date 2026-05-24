# 7) First Non-Repeating Element ⭐
# Question

# Find first element that appears only once.

# Example:

# arr = [4,5,1,2,1,2]

# Output:
# 4

# Algorithm

# Count frequencies.
# Traverse array again.
# First element with frequency 1 is answer.

def firstNonRepeatingEl(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for i in freq:
        if freq[i] == 1:
            return i
    
    return -1

print(firstNonRepeatingEl([4,5,1,2,1,2])) #4
print(firstNonRepeatingEl([1,1,2,2]))  #-1