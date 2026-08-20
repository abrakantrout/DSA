"""
Problem: Kth Largest Element in an Array
LeetCode: 215
Difficulty: Medium

Topic:
- Heap
- Priority Queue

Approach:
- Maintain a min-heap containing the k largest elements seen so far.
- Push each number into the heap.
- If the heap grows larger than k, remove the smallest element.
- After processing all elements, the smallest element in the heap
  is the kth largest element.

Time Complexity: O(n log k)
Space Complexity: O(k)
"""

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]