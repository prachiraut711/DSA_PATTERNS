# Find Duplicate Elements in an Array

# Algorithm

# Create hashmap.
# Traverse array.
# If element already exists:
# print duplicate
# Else:
# store it in hashmap.

def findDuplicate(arr):
    freq = {}

    for i in arr:
        if i in freq:
            print(i)
        else:
            freq[i] = 1
    
    
#here above already has print function so just call function as we not return anything . id we print below then it give output and then NONE
findDuplicate([1,2,2,3,4,1])