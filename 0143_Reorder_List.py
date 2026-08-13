"""
Problem: Reorder List
LeetCode: 143
Difficulty: Medium

Topic:
- Linked List
- Fast & Slow Pointers
- Reversal
- Two Pointers

Approach:
- Find the middle of the linked list using fast and slow pointers.
- Split the list into two halves.
- Reverse the second half.
- Merge the first and reversed second halves alternately.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        # Reverse the second half
        current = second
        prev = None

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        second = prev

        # Merge the two halves
        first = head

        while second:
            next1 = first.next
            next2 = second.next

            first.next = second
            second.next = next1

            first = next1
            second = next2

        return