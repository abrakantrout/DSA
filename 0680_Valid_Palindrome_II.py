"""
Problem: Valid Palindrome II
LeetCode: 680
Difficulty: Easy

Topic:
- String
- Two Pointers

Approach:
- Use two pointers from both ends of the string.
- If characters match, continue moving inward.
- On the first mismatch, try:
  - Skipping the left character, or
  - Skipping the right character.
- If either resulting substring is a palindrome, return True.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipL = s[l + 1:r + 1]
                skipR = s[l:r]

                return (
                    skipL == skipL[::-1]
                    or skipR == skipR[::-1]
                )

            l, r = l + 1, r - 1

        return True