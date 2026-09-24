"""
Problem: Number of Provinces
LeetCode: 547
Difficulty: Medium

Topic:
- Graphs
- DFS
- Adjacency Matrix
- Connected Components

Approach:
- Each city represents a graph node.
- isConnected[node][neighbor] == 1 means there is an edge
  between the two cities.
- Run DFS from every unvisited city.
- Each new DFS represents one connected component (province).
- Track visited cities using a set.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(node):
            visited.add(node)

            for neighbor in range(n):
                if isConnected[node][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)

        for city in range(n):
            if city not in visited:
                provinces += 1
                dfs(city)

        return provinces