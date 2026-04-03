#Insertion Sort

# Idea
# Build sorted array one element at a time (like sorting cards).

# 🧠 Approach
# Start from index 1
# Insert element into correct position in sorted part

def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i] 
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = temp

    return arr

print(insertionSort([5, 3, 4]))
print(insertionSort([4, 1, 3, 9, 7]))


# 📌 Example

# Input: [5, 3, 4]

# Step 1 → [3, 5, 4]
# Step 2 → [3, 4, 5]

# ⏱ Complexity
# Worst: O(n²)
# Best: O(n) (already sorted)