# 349. Intersection of Two Arrays
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

# Algorithm
# Store elements of first array in hashmap.
# Traverse second array.
# If element exists and not already added:
# add to result


def intersection(nums1, nums2):
    freq = {}
    for num in nums1:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    res = []
    for i in nums2:
        if i in freq and i not in res:
            res.append(i)
    
    return res

print(intersection([1,2,2,1], [2,2]))  #[2]
print(intersection([4,9,5], [9,4,9,8,4]))  #[4,9] or [9,4]


print("_________________")
#beeter optimized approch
def intersection(nums1, nums2):

    freq = {}

    # Store elements of nums1
    for num in nums1:
        freq[num] = 1

    added = {}
    res = []

    # Traverse nums2
    for num in nums2:

        if num in freq and num not in added:
            res.append(num)
            added[num] = 1

    return res


print(intersection([1,2,2,1], [2,2]))          # [2]
print(intersection([4,9,5], [9,4,9,8,4]))      # [9,4]