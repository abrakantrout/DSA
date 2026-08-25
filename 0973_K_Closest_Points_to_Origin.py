"""
Problem: K Closest Points to Origin
LeetCode: 973
Difficulty: Medium

Topic:
- Heap
- Priority Queue
- Max Heap

Approach:
- Calculate the squared Euclidean distance of each point from the origin.
- Maintain a max-heap containing the k closest points.
- Use negative distances because Python's heapq provides a min-heap.
- If the heap contains more than k points, remove the farthest point.
- The remaining points are the k closest points to the origin.

Time Complexity: O(n log k)
Space Complexity: O(k)
"""

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            distance = x * x + y * y

            heapq.heappush(heap, (-distance, x, y))

            if len(heap) > k:
                heapq.heappop(heap)

        result = [[x, y] for _, x, y in heap]

        return result