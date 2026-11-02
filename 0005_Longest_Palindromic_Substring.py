
"""
Problem: Longest Palindromic Substring
LeetCode: 5
Difficulty: Medium

Topic:
- Strings
- Two Pointers
- Expand Around Center

Approach:
- Consider every index as the center of a possible palindrome.
- Check both odd-length and even-length palindromes.
- For odd-length palindromes, start with left = right = i.
- For even-length palindromes, start with left = i and right = i + 1.
- Expand outward while the characters match and the pointers
  remain within the string.
- Whenever a longer palindrome is found, update start and max_len.
- Return the longest palindromic substring.

Time Complexity: O(n²)
Space Complexity: O(1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_len = 0

        for i in range(len(s)):

            # Odd-length palindrome
            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    start = left
                    max_len = right - left + 1

                left -= 1
                right += 1

            # Even-length palindrome
            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    start = left
                    max_len = right - left + 1

                left -= 1
                right += 1

        return s[start:start + max_len]
