"""
Problem: Network Delay Time
LeetCode: 743
Difficulty: Medium

Topic:
- Graphs
- Dijkstra's Algorithm
- Shortest Path
- Heap / Priority Queue

Approach:
- Build a weighted directed adjacency list.
- Use Dijkstra's algorithm starting from node k.
- The heap always gives us the currently closest node.
- Relax the edges of each processed node.
- The answer is the maximum shortest distance because the signal
  must reach every node.
- If any node remains unreachable, return -1.

Time Complexity: O((V + E) log V)
Space Complexity: O(V + E)
"""

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}

        for u, v, w in times:
            graph[u].append((v, w))

        distance = [float('inf')] * (n + 1)
        distance[k] = 0

        heap = [(0, k)]

        while heap:
            cur_dist, node = heapq.heappop(heap)

            if cur_dist > distance[node]:
                continue

            for neighbor, w in graph[node]:
                new_dist = cur_dist + w

                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

        ans = max(distance[1:])

        if ans == float('inf'):
            return -1

        return ans