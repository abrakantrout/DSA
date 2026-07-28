"""
Problem: Reverse Linked List
LeetCode: 206
Difficulty: Easy

Topic:
- Linked List

Approach:
- Use three pointers:
  - 'prev' points to the previous node.
  - 'current' points to the current node.
  - 'next' stores the next node before changing links.
- Reverse the direction of each pointer while traversing the list.
- Return 'prev' as the new head of the reversed list.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev