#Selection Sort

# Idea

# Find the minimum element and place it at correct position.

# 🧠 Approach
# Pick index i
# Find smallest from i → n
# Swap with i

def selctionSort(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
            
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
    return arr

print(selctionSort([4, 1, 3, 9, 7]))
print(selctionSort([4, 2, 5, 1]))
print("____")

#approch 2 using temp
def selectionSort(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        
        if min != i:
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp

    return arr
print(selctionSort([4, 1, 3, 9, 7]))
print(selctionSort([4, 2, 5, 1]))
