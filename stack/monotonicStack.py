# python file-  bagh detail sathi

#monotonic increasing stack used in -- Next smaller, previous smaller, histogram or area of largest reactangle, remove k digit
#monoting Decreasing stack used in -next greater, previous greater, daily temperature, stock span problem


#monotonic incresing stack
def monotonicIncreasing(nums):
    stack = []
    for i in nums:
        while stack and stack[-1] > i:
            stack.pop()
        stack.append(i)
    return stack

print(monotonicIncreasing([3, 1, 4, 1, 5, 9, 2, 6]))   #output should be [1, 1, 2, 6]


#monotonic decresing stack
def monotonicDecresing(nums):
    stack = []
    for i in nums:
        while stack and stack[-1] < i:
            stack.pop()
        stack.append(i)
    return stack

print(monotonicDecresing([3, 1, 4, 1, 5, 9, 2, 6])) ##output should be [9,6]