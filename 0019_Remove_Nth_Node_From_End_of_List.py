"""
Problem: Remove Nth Node From End of List
LeetCode: 19
Difficulty: Medium

Topic:
- Linked List
- Two Pointers

Approach:
- Create a dummy node pointing to the head to simplify edge cases.
- Initialize both slow and fast pointers at the dummy node.
- Move the fast pointer n + 1 steps ahead.
- Move both pointers together until the fast pointer reaches the end.
- The slow pointer will be just before the node to remove.
- Skip the target node and return the updated list.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(
        self,
        head: Optional[ListNode],
        n: int
    ) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        slow = dummy
        fast = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next