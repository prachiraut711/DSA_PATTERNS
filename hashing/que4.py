# 4) Check if Two Arrays are Equal
# Question

# Check whether two arrays contain same elements with same frequencies.

# Example:

# arr1 = [1,2,2,3]
# arr2 = [2,1,3,2]

# Output:

# True
# Algorithm
# If lengths different:
# return False
# Count frequency of arr1.
# Traverse arr2:
# reduce frequency
# If any frequency becomes negative:
# return False
# Else arrays are equal.

def arrayEqual(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    
    freq = {}
    for num in arr1:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for num in arr2:
        if num not in freq:
            return False
        
        freq[num] -= 1

        if freq[num] < 0:
            return False
    
    return True

print(arrayEqual([1,2,3,2], [2,1,2,3]))   #true
print(arrayEqual([1,2,3,4], [2,1,2,3]))   #false

print("_________")




#method 2
def arrayEqual(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    
    freq = {}
    for num in arr1:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    freq2 = {}
    for num in arr2:
        if num in freq2:
            freq2[num] += 1
        else:
            freq2[num] = 1

    if freq == freq2:
        return True
    else:
        return False
    
print(arrayEqual([1,2,3,2], [2,1,2,3]))   #true
print(arrayEqual([1,2,3,4], [2,1,2,3]))   #false