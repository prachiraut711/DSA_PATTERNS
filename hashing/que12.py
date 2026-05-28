# 202. Happy Number

# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.


# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Example 2:

# Input: n = 2
# Output: false
#2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4  
#here in this example the 4  repepeats and same cycle again occur so we keep hashmap to track the repeatness of number
# Now 4 repeats forever.

# Infinite loop happens.

# So we use hashing/set to detect repeated numbers.

def happyNumber(n):
    seen = {}

    while n != 1:  #as 1 cha sqqure 1 mag tech tech yeil so num should be greater than 1
        if n in seen:
            return False    #this condition and hashmap for example to as infinite loop happens in some case so we track the num is reapeated or not by using hash map
        seen[n] = 1

        total = 0
        
        while n > 0:
            digit = n % 10
            total += digit * digit
            n = n // 10

        n = total

    return True

print(happyNumber(19)) #True
print(happyNumber(2)) #False
