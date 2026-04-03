#bubble sort

# Idea
# Repeatedly swap adjacent elements if they are in the wrong order.

# 🧠 Approach
# Compare arr[i] and arr[i+1]
# Swap if arr[i] > arr[i+1]
# After each pass → largest element moves to the end

#approch 1 (using temp)
def bubbleSort(arr):
    for i in range(len(arr) - 1):
        flag = 0
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                flag = 1
            
        if flag == 0:   #hw j chya loop natar check karych for redundation means jar ek pan swap nahi zla 1st pass madhe tar mag already sorted na break kel
            break

    return arr

print(bubbleSort([5,3,8,4,6]))
print(bubbleSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))

print("_____")

#approch 2 (same just direct swap)
def bubbleSort(arr):
    for i in range(len(arr) - 1):
        swapped = 0
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = 1
        
        if swapped == 0:
            break

    return arr

print(bubbleSort([5,3,8,4,6]))
print(bubbleSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))