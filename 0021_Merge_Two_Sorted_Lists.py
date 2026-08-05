"""
Problem: Merge Two Sorted Lists
LeetCode: 21
Difficulty: Easy

Topic:
- Linked List

Approach:
- Create a dummy node to simplify list construction.
- Maintain a tail pointer to build the merged list.
- Compare the current nodes of both lists and append the smaller node.
- Move the corresponding list pointer forward.
- Once one list is exhausted, append the remaining nodes of the other list.

Time Complexity: O(n + m)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next