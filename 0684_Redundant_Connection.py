"""
Problem: Redundant Connection
LeetCode: 684
Difficulty: Medium

Topic:
- Graphs
- Union-Find
- Disjoint Set Union (DSU)
- Cycle Detection

Approach:
- Initially, every node belongs to its own connected component.
- Use Union-Find to track which nodes are already connected.
- For each edge, find the roots of both endpoints.
- If both endpoints already have the same root, adding the edge
  would create a cycle, so it is the redundant connection.
- Otherwise, merge the two components using union by size.
- Path compression makes future find operations faster.

Time Complexity: O(n * α(n)) ≈ O(n)
Space Complexity: O(n)
"""

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = list(range(n + 1))
        size = [1] * (n + 1)

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

        for a, b in edges:
            if not union(a, b):
                return [a, b]