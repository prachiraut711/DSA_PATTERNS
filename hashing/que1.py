# Count Frequency of Elements in an Array


def countFreq(arr):
    freq = {}

    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    return freq

print(countFreq([1,2,2,3,2,4,4,5]))
print(countFreq([1,2,2,1]))
print(countFreq([1,2,3,4]))