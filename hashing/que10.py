# 10) Union of Two Arrays
# Question

# Return all unique elements from both arrays.

# Example:

# arr1 = [1,2,3]
# arr2 = [2,3,4]

# Output:

# [1,2,3,4]
# Algorithm
# Create hashmap.
# Insert all elements from first array.
# Insert all elements from second array.
# Return keys.

def unionArray(arr1, arr2):

    union = {}

    for num in arr1:
        union[num] = 1

    for num in arr2:
        union[num] = 1

    result = []

    for key in union:
        result.append(key)

    return result


arr1 = [1, 2, 3]
arr2 = [2, 3, 4]

print(unionArray(arr1, arr2))

print("_____________")
#this is correct but for some case its wrong 
def union(arr1, arr2):
    freq = {}
    for num in arr1:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for i in arr2:
        if i not in freq:
            arr1.append(i)

    return arr1

print(union([1,2,3], [2,3,4]))  #[1,2,3,4]