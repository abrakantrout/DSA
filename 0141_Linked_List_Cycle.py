"""
Problem: Linked List Cycle
LeetCode: 141
Difficulty: Easy

Topic:
- Linked List
- Fast & Slow Pointers
- Floyd's Cycle Detection

Approach:
- Use two pointers starting at the head.
- The slow pointer moves one node at a time.
- The fast pointer moves two nodes at a time.
- If a cycle exists, the two pointers will eventually meet.
- If the fast pointer reaches None, there is no cycle.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False