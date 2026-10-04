"""
Problem: Minimum Cost to Make at Least One Valid Path in a Grid
LeetCode: 1368
Difficulty: Hard

Topic:
- Graphs
- 0-1 BFS
- Shortest Path
- Deque

Approach:
- Each cell is treated as a graph node.
- Moving in the direction indicated by the current cell costs 0.
- Changing the direction costs 1.
- Since every edge has a weight of either 0 or 1, use 0-1 BFS.
- If the movement costs 0, add the cell to the front of the deque.
- If the movement costs 1, add the cell to the back.
- Maintain the minimum cost required to reach every cell.

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        distance = [[float('inf')] * cols for _ in range(rows)]
        queue = deque([(0, 0)])

        distance[0][0] = 0

        directions = [
            (0, 1, 1),
            (0, -1, 2),
            (1, 0, 3),
            (-1, 0, 4)
        ]

        while queue:
            r, c = queue.popleft()

            for dr, dc, required_direction in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:

                    if grid[r][c] == required_direction:
                        cost = 0
                    else:
                        cost = 1

                    new_dist = distance[r][c] + cost

                    if new_dist < distance[nr][nc]:
                        distance[nr][nc] = new_dist

                        if cost == 0:
                            queue.appendleft((nr, nc))
                        else:
                            queue.append((nr, nc))

        return distance[rows - 1][cols - 1]