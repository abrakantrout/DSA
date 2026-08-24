"""
Problem: Find Median from Data Stream
LeetCode: 295
Difficulty: Hard

Topic:
- Heap
- Priority Queue
- Two Heaps
- Data Stream

Approach:
- Maintain two heaps:
  - left: max-heap containing the smaller half of the numbers.
  - right: min-heap containing the larger half of the numbers.
- Python provides a min-heap, so negative values are used to simulate
  a max-heap for the left heap.
- Keep the heaps balanced so that their sizes differ by at most one.
- The median is either the top of the larger heap or the average of
  both heap tops when their sizes are equal.

Time Complexity:
- addNum: O(log n)
- findMedian: O(1)

Space Complexity: O(n)
"""

import heapq

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if not self.left or num <= -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)

        if len(self.left) > len(self.right) + 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)

        if len(self.right) > len(self.left):
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            median = (-self.left[0] + self.right[0]) / 2
        else:
            median = -self.left[0]

        return median