"""
Problem: Last Stone Weight
LeetCode: 1046
Difficulty: Easy

Topic:
- Heap
- Priority Queue
- Max Heap

Approach:
- Python provides a min-heap, so store negative values to simulate
  a max-heap.
- Repeatedly remove the two heaviest stones.
- If their weights are different, push the remaining difference back.
- Continue until at most one stone remains.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            val1 = -heapq.heappop(heap)
            val2 = -heapq.heappop(heap)

            result = val1 - val2

            if result > 0:
                heapq.heappush(heap, -result)

        return -heap[0] if heap else 0