"""
Problem: Remove Linked List Elements
LeetCode: 203
Difficulty: Easy

Topic:
- Recursion
- Linked List

Approach:
- Recursively process the rest of the linked list first.
- After the recursive call returns, check the current node.
- If the current node's value equals val, skip the current node
  by returning head.next.
- Otherwise, keep the current node.

Time Complexity: O(n)
Space Complexity: O(n)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(
        self,
        head: Optional[ListNode],
        val: int
    ) -> Optional[ListNode]:

        if head is None:
            return None

        head.next = self.removeElements(head.next, val)

        if head.val == val:
            return head.next

        return head