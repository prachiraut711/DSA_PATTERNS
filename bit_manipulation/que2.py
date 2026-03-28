#Check if i-th Bit is Set

# Given two positive integer n and  i, check if the ith index bit of n is set or not.

#  Note: A bit is called set if it is 1.

def check_ith_bit(n, i):
    if n & (1 << i):
        return "SET"
    else:
        return "NOT SET"

print(check_ith_bit(5, 0))
print(check_ith_bit(5, 1))   

# 5 => 101 so check 101 & 000 = 0 and 101 & 001 = 1 