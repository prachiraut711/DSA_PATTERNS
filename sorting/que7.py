#quick sort

def quickSort(arr):
    def sort(low, high):
        if low < high:
            pivot = partition(arr, low, high)
            sort(low, pivot - 1)
            sort(pivot + 1, high)

    def partition(arr, low, high):
        p = arr[low]
        i = low + 1
        j = high

        while True:
            while i <= j and arr[i] <= p:
                i += 1
            while i <= j and arr[j] >= p:
                j -= 1

            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break

        arr[low], arr[j] = arr[j], arr[low]
        return j
    
    sort(0, len(arr) - 1)
    return arr
    
print(quickSort([4,1,3,2]))

print("____________")
#another approch

def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)
    return arr

def partition(arr, low, high):
    p = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= p:
            i += 1
        while i <=j and arr[j] >= p:
            j -= 1
        
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j


arr = [4, 1, 2, 3]
print(quickSort(arr, 0, len(arr) - 1))
