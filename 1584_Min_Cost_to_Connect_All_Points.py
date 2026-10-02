"""
Problem: Min Cost to Connect All Points
LeetCode: 1584
Difficulty: Medium

Topic:
- Graphs
- Minimum Spanning Tree
- Kruskal's Algorithm
- Union-Find / DSU

Approach:
- Treat every point as a graph node.
- Create an edge between every pair of points.
- The edge weight is the Manhattan distance between the points.
- Sort all edges by weight.
- Use Kruskal's Algorithm to repeatedly choose the cheapest edge
  that connects two different components.
- Union the components using DSU.
- Stop after selecting n - 1 edges, since a spanning tree contains
  exactly n - 1 edges.

Time Complexity: O(n^2 log n)
Space Complexity: O(n^2)
"""

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        edges = []

        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                weight = abs(x1 - x2) + abs(y1 - y2)
                edges.append((i, j, weight))

        edges.sort(key=lambda x: x[2])

        parent = list(range(n))
        size = [1] * n

        def find(x):
            if x == parent[x]:
                return x

            parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return False

            if size[rootA] < size[rootB]:
                rootA, rootB = rootB, rootA

            parent[rootB] = rootA
            size[rootA] += size[rootB]

            return True

        total = 0
        count = 0

        for a, b, weight in edges:
            if not union(a, b):
                continue

            total += weight
            count += 1

            if count == n - 1:
                break

        return total