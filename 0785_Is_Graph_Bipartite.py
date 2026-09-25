"""
Problem: Is Graph Bipartite?
LeetCode: 785
Difficulty: Medium

Topic:
- Graphs
- DFS
- Graph Coloring
- Bipartite Graph

Approach:
- Assign each node one of two colors: 0 or 1.
- For every node, assign the opposite color to its neighbors.
- If a neighbor already has the same color as the current node,
  the graph cannot be bipartite.
- Run DFS from every unvisited node because the graph may be disconnected.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        color = {}

        def dfs(node, curr_color):
            color[node] = curr_color

            for neighbor in graph[node]:
                if neighbor not in color:
                    if not dfs(neighbor, 1 - curr_color):
                        return False

                elif color[neighbor] == color[node]:
                    return False

            return True

        for i in range(len(graph)):
            if i not in color:
                if not dfs(i, 0):
                    return False

        return True