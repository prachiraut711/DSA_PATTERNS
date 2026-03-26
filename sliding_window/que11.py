# 904. Fruit Into Baskets

# You are visiting a farm that has a single row of fruit trees arranged from left to right. 
# The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# 1.You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# 2.Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. 
# The picked fruits must fit in one of your baskets.
# 3.Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.


# Example 1:

# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
# Example 2:

# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
# Example 3:

# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].


# 🧠 1. Understanding the Question (Simple Words)

# You have:

# An array fruits → each number = type of fruit

# Rules:

# You have only 2 baskets
# Each basket can hold only ONE type of fruit
# You must pick fruits continuously (subarray)

# 👉 Stop when you encounter a third type

# 🎯 Goal

# Find the maximum number of fruits you can collect

# 👉 i.e., longest subarray with at most 2 distinct numbers

# 🔍 Example
# fruits = [1,2,3,2,2]

# Valid subarrays:

# [1,2] → 2 types
# [2,3,2,2] → 2 types ✅ (length = 4)

# 👉 Answer = 4

# 💡 2. Brute Force Approach
# Idea:
# Try all subarrays
# Check number of distinct fruits
# If ≤ 2 → update max
# Complexity:
# Time: O(n²) ❌ too slow
# 🚀 3. Optimal Approach (Sliding Window)
# 🔑 Key Idea

# 👉 Maintain a window with:

# at most 2 distinct fruit types
# Condition:
# len(set(window)) <= 2

# If > 2 → shrink window

# 📌 4. Algorithm (Step-by-Step)
# Initialize:
# left = 0
# count_map = {}
# max_len = 0
# Loop right from 0 → n:
# Add fruits[right] to map
# If map size > 2:
# Shrink window
# Reduce count of fruits[left]
# Remove if count = 0
# Move left

# Update:

# max_len = max(max_len, right - left + 1)


#ithe basically 2 basket chi condition ahe mahnje k = 2 mahnun ha sliding window problem ahe
def totalFruit(fruits):
    left = 0 
    max_len = 0
    count_map = {}

    for right in range(len(fruits)):
        fruit = fruits[right]

        if fruit in count_map:
            count_map[fruit] += 1
        else:
            count_map[fruit] = 1
        
        while len(count_map) > 2:
            left_fruit = fruits[left]
            count_map[left_fruit] -= 1
            if count_map[left_fruit] == 0:
                del count_map[left_fruit]
            left += 1
        
        max_len = max(max_len, right -left + 1)
    
    return max_len

print(totalFruit([1,2,1]))
print(totalFruit([0,1,2,2]))
print(totalFruit([1,2,3,2,2]))