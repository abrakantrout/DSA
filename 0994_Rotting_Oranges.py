"""
Problem: Rotting Oranges
LeetCode: 994
Difficulty: Medium

Topic:
- Graphs
- BFS
- Multi-Source BFS
- Matrix

Approach:
- Add all initially rotten oranges to the queue.
- Count the number of fresh oranges.
- Process the queue level by level.
- Each BFS level represents one minute.
- When a rotten orange reaches a fresh orange, make it rotten
  and add it to the queue.
- Continue until there are no fresh oranges left or no more
  oranges can be reached.
- If fresh oranges remain, return -1.

Time Complexity: O(rows * cols)
Space Complexity: O(rows * cols)
"""

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        queue = deque()
        fresh_count = 0
        minutes = 0

        directions = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    queue.append((r, c))

                elif grid[r][c] == 1:
                    fresh_count += 1

        while queue and fresh_count > 0:
            level_size = len(queue)

            while level_size:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh_count -= 1
                            queue.append((nr, nc))

                level_size -= 1

            minutes += 1

        if fresh_count > 0:
            return -1

        return minutes