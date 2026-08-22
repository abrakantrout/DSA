"""
Problem: Top K Frequent Elements
LeetCode: 347
Difficulty: Medium

Topic:
- Heap
- Priority Queue
- Hash Map
- Frequency Counting

Approach:
- Count the frequency of each number using Counter.
- Maintain a min-heap containing the k most frequent elements.
- Push each (frequency, number) pair into the heap.
- If the heap grows larger than k, remove the least frequent element.
- The remaining elements in the heap are the k most frequent elements.

Time Complexity: O(n log k)
Space Complexity: O(n)
"""

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)

        result = [num for count, num in heap]

        return result