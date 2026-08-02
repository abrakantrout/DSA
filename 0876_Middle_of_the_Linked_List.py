"""
Problem: Middle of the Linked List
LeetCode: 876
Difficulty: Easy

Topic:
- Linked List
- Fast & Slow Pointers

Approach:
- Use two pointers:
  - 'slow' moves one node at a time.
  - 'fast' moves two nodes at a time.
- When the fast pointer reaches the end of the list,
  the slow pointer will be at the middle node.
- If there are two middle nodes, return the second one.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow