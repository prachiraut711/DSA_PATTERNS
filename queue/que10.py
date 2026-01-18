# 994. Rotting Oranges

# You are given an m x n grid where each cell can have one of three values:
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Example 1:

# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.

# **What the Question Wants (Simple Explanation)

# You are given a grid where each cell represents an orange:

# Value	Meaning
# 0	Empty cell
# 1	Fresh orange
# 2	Rotten orange
# Rule

# Every minute, a rotten orange turns its adjacent fresh oranges
# (up, down, left, right) rotten.

# 🎯 Goal

# Return the minimum number of minutes needed so that all fresh oranges become rotten.

# If it’s impossible, return -1

# If there are no fresh oranges, return 0

# 🧠 Key Idea (Why BFS?)

# This is a multi-source BFS problem:

# All initial rotten oranges act as starting points

# Rotting spreads level by level → each level = 1 minute

# ✅ Correct Algorithm

# Traverse the grid

# Count fresh oranges

# Push all rotten oranges into a queue

# Run BFS

# For each minute:

# Rot one layer of oranges

# Decrease fresh count

# Stop when:

# No fresh oranges left → return time

# BFS ends but fresh still exist → return -1

#IT IS USED BFS + QUEUE 
from collections import deque
def rottingOrange(grid):
    rows = len(grid)
    col = len(grid[0])
    q = deque()
    fresh = 0

    for r in range(rows):
        for c in range(col):
            if grid[r][c] == 2:
                q.append((r,c))
            elif grid[r][c] == 1:
                fresh += 1

    if fresh == 0:
        return 0
    
    minutes = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while q and fresh > 0:
        minutes += 1

        for _ in range(len(q)):
            r, c = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < col and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr,nc))

    
    return minutes if fresh == 0 else -1

print(rottingOrange([[2,1,1],[1,1,0],[0,1,1]]))
print(rottingOrange([[2,1,1],[0,1,1],[1,0,1]]))
print(rottingOrange([[0,2]]))

        


