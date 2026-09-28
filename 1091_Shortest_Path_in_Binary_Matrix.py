"""
Problem: Shortest Path in Binary Matrix
LeetCode: 1091
Difficulty: Medium

Topic:
- Graphs
- BFS
- Shortest Path
- Matrix

Approach:
- Treat each open cell (0) as a graph node.
- From each cell, we can move in 8 directions.
- BFS is used because every move has the same cost of 1.
- Process the queue level by level, where each level represents
  one additional step in the path.
- Mark cells as visited by changing them from 0 to 1.
- Return the distance when the bottom-right cell is reached.

Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        queue = deque([(0, 0)])
        dist = 1

        grid[0][0] = 1

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                r, c = queue.popleft()

                if r == n - 1 and c == n - 1:
                    return dist

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        queue.append((nr, nc))

            dist += 1

        return -1