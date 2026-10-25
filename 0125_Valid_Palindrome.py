
"""
Problem: Valid Palindrome
LeetCode: 125
Difficulty: Easy

Topic:
- Strings
- Two Pointers

Approach:
- Convert the string to lowercase.
- Use two pointers, one starting at each end of the string.
- Skip characters that are not alphanumeric.
- Compare the characters at both pointers.
- If they differ, return False.
- If they match, move both pointers inward.
- If all comparisons succeed, return True.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s = s.lower()

        while l < r:
            if not s[l].isalnum():
                l += 1

            elif not s[r].isalnum():
                r -= 1

            elif s[l] == s[r]:
                l += 1
                r -= 1

            else:
                return False

        return True
