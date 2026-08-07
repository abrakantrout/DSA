"""
Problem: Reverse Nodes in k-Group
LeetCode: 25
Difficulty: Hard

Topic:
- Linked List
- Pointer Manipulation

Approach:
- Use a dummy node to simplify reconnecting reversed groups.
- Find the kth node from the previous group's end.
- If fewer than k nodes remain, leave them unchanged.
- Reverse exactly k nodes.
- Reconnect the reversed group to the previous and next groups.
- Repeat until the list is fully processed.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(
        self,
        head: Optional[ListNode],
        k: int
    ) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        dummy = ListNode()
        dummy.next = head

        prev = dummy
        first = head

        while True:
            kth = prev

            for _ in range(k):
                kth = kth.next

                if kth is None:
                    return dummy.next

            next_group = kth.next

            prev_node = next_group
            current = first

            while current != next_group:
                next_node = current.next
                current.next = prev_node
                prev_node = current
                current = next_node

            prev.next = prev_node

            prev = first
            first = next_group
