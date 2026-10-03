"""
Problem: Min Cost to Connect All Points
LeetCode: 1584
Difficulty: Medium

Topic:
- Graphs
- Minimum Spanning Tree
- Prim's Algorithm
- Greedy

Approach:
- Treat every point as a node in a complete graph.
- The cost of connecting two points is their Manhattan distance.
- Start with point 0 and gradually build the Minimum Spanning Tree.
- min_dist[i] stores the minimum cost currently known to connect
  point i to the existing MST.
- At each step, choose the unvisited point with the smallest
  connection cost.
- Add that cost to the total and update the connection costs
  of the remaining unvisited points.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)

        visited = [False] * n
        min_dist = [float('inf')] * n

        min_dist[0] = 0
        total = 0

        for _ in range(n):
            min_cost = float('inf')
            current = -1

            for i in range(n):
                if not visited[i] and min_dist[i] < min_cost:
                    min_cost = min_dist[i]
                    current = i

            visited[current] = True
            total += min_cost

            for i in range(n):
                if not visited[i]:
                    x1, y1 = points[current]
                    x2, y2 = points[i]

                    cost = abs(x1 - x2) + abs(y1 - y2)

                    if cost < min_dist[i]:
                        min_dist[i] = cost

        return total