"""
Problem: Reverse String
LeetCode: 344
Difficulty: Easy

Topic:
- String
- Two Pointers

Approach:
- Use two pointers, one at the beginning and one at the end.
- Swap the characters at both pointers.
- Move the left pointer forward and the right pointer backward.
- Continue until the pointers meet.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1