"""
Problem: Swap Nodes in Pairs
LeetCode: 24
Difficulty: Medium

Topic:
- Linked List

Approach:
- Use a dummy node to simplify swapping the head pair.
- Maintain a pointer to the node before the current pair.
- Swap each adjacent pair by updating their next pointers.
- Move to the next pair and repeat until fewer than two nodes remain.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode()
        dummy.next = head

        prev = dummy
        first = head

        while first and first.next:
            second = first.next
            next_pair = second.next

            prev.next = second
            second.next = first
            first.next = next_pair

            prev = first
            first = next_pair

        return dummy.next