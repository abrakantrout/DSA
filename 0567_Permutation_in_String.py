
"""
Problem: Permutation in String
LeetCode: 567
Difficulty: Medium

Topic:
- Strings
- Sliding Window
- Frequency Array

Approach:
- If s1 is longer than s2, return False.
- Build frequency arrays for s1 and the first window of s2.
- Compare the frequency arrays.
- Slide the fixed-size window through s2 by adding the incoming
  character and removing the outgoing character.
- Return True when both frequency arrays match.

Time Complexity: O(n + m)
Space Complexity: O(1)
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        m = len(s1)
        n = len(s2)

        s1_freq = [0] * 26
        win_freq = [0] * 26

        for i in range(m):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            win_freq[ord(s2[i]) - ord('a')] += 1

        if s1_freq == win_freq:
            return True

        for right in range(m, n):
            incoming = ord(s2[right]) - ord('a')
            outgoing = ord(s2[right - m]) - ord('a')

            win_freq[incoming] += 1
            win_freq[outgoing] -= 1

            if s1_freq == win_freq:
                return True

        return False
