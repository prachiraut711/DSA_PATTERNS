# 5) Check if Two Strings are Anagrams ⭐

# (LeetCode 242)

# Question

# Two strings are anagrams if both contain same characters with same frequency.

# Example:

# s = "listen"
# t = "silent"

# Output:

# True
# Algorithm
# If lengths differ:
# return False
# Count characters of first string.
# Traverse second string:
# reduce count
# If character missing or count negative:
# return False
# Otherwise True.

def checkAnagram(str1, str2):
    if len(str1) != len(str2):
        return False
    
    freq = {}
    for i in str1:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    for i in str2:
        if i not in freq:
            return False
        
        freq[i] -= 1

        if freq[i] < 0:
            return False
        
    return True

print(checkAnagram("listen", "silent")) #true
print(checkAnagram("prachi", "rachi"))  #false
print(checkAnagram("eat", "ate"))  #true


print("_____________")

#method 2

def checkAnagram(str1, str2):
    if len(str1) != len(str2):
        return False
    
    freq1 = {}
    for i in str1:
        if i in freq1:
            freq1[i] += 1
        else:
            freq1[i] = 1

    freq2 = {}
    for i in str2:
        if i in freq2:
            freq2[i] += 1
        else:
            freq2[i] = 1
    
    
    if freq1 == freq2:
        return True
    else:
        return False

print(checkAnagram("listen", "silent")) #true
print(checkAnagram("prachi", "rachi"))  #false
print(checkAnagram("eat", "ate"))  #true
