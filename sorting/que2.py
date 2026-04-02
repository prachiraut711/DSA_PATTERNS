# 4. Check if Array is Sorted
# ✅ Idea

# Check if every element is ≤ next element.

# 🧠 Approach
# Traverse once
# If arr[i] > arr[i+1] → Not sorted

def is_sorted(nums):
    for i in range(len(nums) - 1):  #ithe i + 1 check kartoy na mag len(nums) getl tar i + 1 nahi yenar so len(nums) - 1 getl
        if nums[i] > nums[i + 1]:
            return False
    return True

print(is_sorted([1,2,3,4]))
print(is_sorted([8,7,6,5]))