"""
Problem: Number of Islands
LeetCode: 200
Difficulty: Medium

Topic:
- Graphs
- DFS
- Matrix
- Connected Components

Approach:
- Treat each land cell ("1") as a node in a graph.
- From every unvisited land cell, run DFS to visit the entire
  connected island.
- Mark visited land cells as "0" so they are not processed again.
- Each new DFS started represents one separate island.

Time Complexity: O(rows * cols)
Space Complexity: O(rows * cols) in the worst case due to DFS recursion
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or
                c >= cols or grid[r][c] == "0"):
                return

            grid[r][c] = "0"

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands