# 49. Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

# Algorithm
# Sort each string.
# Use sorted string as hashmap key.
# Store all matching words together.

def groupAnagrams(strs):
    groups = {}

    for word in strs:
        sorted_word = "".join(sorted(word))

        if sorted_word in groups:
            groups[sorted_word].append(word)
        else:
            groups[sorted_word] = [word]    #ithe [word] kar jar nust word lihl tar error yeil Because each key in groups stores a list of words that belong to the same anagram group.

    
    result = []
    for key in groups:
        result.append(groups[key])

    return result

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))