#same logic as stack

# There are two main types of monotonic queues:

# Increasing Monotonic Queue: It only keeps elements in increasing order, and any element that is smaller than the current minimum is removed.
# Decreasing Monotonic Queue: It only keeps elements in decreasing order, and any element that is larger than the current maximum is removed.

# monotonic incresing queue
from collections import deque
def increasing_monotonic_queue(arr, n):
    q = deque()
    for i in range(n):
        while len(q) > 0 and q[-1] > arr[i]:
            q.pop()
        q.append(arr[i])
    return q

arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
q = increasing_monotonic_queue(arr, n)
for i in q:
    print(i, end=' ')


#monotonic decresing queue - ex Sliding Wndow Maximum
def decreasing_monotonic_queue(arr):
    n = len(arr)
    q = deque()
    for i in range(n):

        # If recently added element is
        # smaller than current element
        while q and q[-1] < arr[i]:

            q.pop()

        q.append(arr[i])

    return q

# Driver Code
arr = [6, 5, 4, 3, 2, 1]

# Function call
q = decreasing_monotonic_queue(arr)

for i in q:
    print(i)