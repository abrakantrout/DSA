"""
Problem: Maximum Number of Vowels in a Substring of Given Length
LeetCode: 1456
Difficulty: Medium

Topic:
- Arrays
- Sliding Window

Approach:
- Maintain a fixed-size window of length k.
- Count vowels as the right pointer moves.
- When the window exceeds k, remove the contribution of
  the leftmost character and move the left pointer.
- Update the maximum vowel count whenever the window
  reaches exactly k characters.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_count = 0
        win_count = 0
        l = 0

        for r in range(len(s)):
            if s[r] in "aeiou":
                win_count += 1

            if (r - l + 1) > k:
                if s[l] in "aeiou":
                    win_count -= 1
                l += 1

            if (r - l + 1) == k:
                max_count = max(win_count, max_count)

        return max_count
