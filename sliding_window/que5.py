# Diet Plan Performance
# 🧾 Problem Description

# A dieter consumes calories[i] calories on the i-th day.

# Given an integer k, for every consecutive sequence of k days (calories[i], calories[i+1], ..., calories[i+k-1] for all 0 <= i <= n-k), let T be the total calories consumed during those k days:

# If T < lower: the dieter performed poorly → lose 1 point

# If T > upper: the dieter performed well → gain 1 point

# If lower <= T <= upper: no change in points

# The dieter starts with zero points.
# Return the total number of points the dieter has after evaluating all possible k-day windows.

# Note: The total points can be negative.

# 📌 Constraints

# 1 <= k <= calories.length <= 10^5

# 0 <= calories[i] <= 20000

# 0 <= lower <= upper

# 🧾 Example 1:
# Input:
# calories = [1,2,3,4,5]
# k = 1
# lower = 3
# upper = 3

# Output: 0

# Explanation:
# Since k = 1, each day is a window.
# Days 0 and 1: calories < 3 → lose 2 points
# Days 3 and 4: calories > 3 → gain 2 points
# Net points = 0


# ✔️ Explanation from sources with same logic.

# 🧾 Example 2:
# Input:
# calories = [3,2]
# k = 2
# lower = 0
# upper = 1

# Output: 1

# Explanation:
# Total calories for window [3,2] is 5 > upper → gain 1 point


# ✔️ Matches community solutions.

# 🧾 Example 3:
# Input:
# calories = [6,5,0,0]
# k = 2
# lower = 1
# upper = 5

# Output: 0

# Explanation:
# Window [6,5] → 11 > upper → +1
# Window [5,0] → 5 in range → 0
# Window [0,0] → 0 < lower → -1
# Net = 1 + 0 - 1 = 0

# **Problem in Simple Words

# You are given daily calories.

# Look at every continuous window of size k.

# For each window:

# If sum < lower → –1 point

# If sum > upper → +1 point

# Else → 0 points

# Start with score = 0

# Return final score.

# This is a Sliding Window problem.


#so basically jevdi window ahe tyachi plus karychi ti sum jar < lower asel tar -1 kel ani jar sum > upper tar +1
def  dietPlanPerformance(calories, k, lower, upper):
    window_sum = 0
    score = 0

    for i in range(k):
        window_sum += calories[i]
    #If lower <= T <= upper: no change in points hi condition dilye que mahe mag T(sum of window) he jar lower kivva upper eaul to ael same asel tar 0 points mag mahnun
    #ithe fakt < lower and > upper kel
    if window_sum < lower:
        score -= 1
    elif window_sum > upper:
        score += 1

    #for other windows
    for i in range(k, len(calories)):
        window_sum += calories[i] - calories[i - k]

        if window_sum < lower:
            score -= 1
        elif window_sum > upper:
            score += 1

    return score

print(dietPlanPerformance([1,2,3,4,5], 1, 3, 3))
print(dietPlanPerformance([3,2], 2, 0, 1))
print(dietPlanPerformance([6,5,0,0], 2, 1, 5))