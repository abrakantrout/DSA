"""
Problem: Clone Graph
LeetCode: 133
Difficulty: Medium

Topic:
- Graphs
- BFS
- Hash Map
- Graph Copy

Approach:
- Use a hash map to store the mapping from each original node
  to its cloned node.
- Start BFS from the given node.
- Whenever an unvisited neighbor is found, create its clone
  and add it to the queue.
- Connect each cloned node to the cloned versions of its neighbors.
- Return the clone of the starting node.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clones = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            current = queue.popleft()

            for neighbor in current.neighbors:

                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                clones[current].neighbors.append(clones[neighbor])

        return clones[node]