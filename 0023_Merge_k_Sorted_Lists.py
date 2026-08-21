"""
Problem: Merge k Sorted Lists
LeetCode: 23
Difficulty: Hard

Topic:
- Heap
- Priority Queue
- Linked List

Approach:
- Add the first node from each non-empty linked list to a min-heap.
- Each heap entry contains the node value, list index, and node itself.
- Repeatedly remove the smallest node from the heap and attach it
  to the merged list.
- If the removed node has a next node, add that node to the heap.
- Continue until all nodes have been processed.

Time Complexity: O(N log k)

where:
- N = total number of nodes across all lists
- k = number of linked lists

Space Complexity: O(k)
"""

import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(
        self,
        lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:

        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)

            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(
                    heap,
                    (node.next.val, i, node.next)
                )

        return dummy.next