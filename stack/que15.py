# 402. Remove K Digits

# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.


# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Example 2:

# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# Example 3:

# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.

def removeKdigits(num, k):
    stack = []
    for i in num:
        while stack and k > 0 and stack[-1] > i:
            stack.pop()
            k -= 1
        stack.append(i)
    # If k still left, remove from end
    while k > 0:
        stack.pop()
        k -= 1
    
    res = "".join(stack).lstrip("0")  #left side cge trailling zero remove karayla as mention in que
    
    if res:   ##ithe res check in last example stack check kel tar if res = "" al tar output pn "" yeil 0 chya jagi so instead if stack: use if res:
        return res
    else:
        return "0" 

print(removeKdigits("1432219", 3))
print(removeKdigits("10200", 1))
print(removeKdigits("10", 2))
print(removeKdigits("10", 1))
