
"""
Problem: Find All Anagrams in a String
LeetCode: 438
Difficulty: Medium

Topic:
- Strings
- Sliding Window
- Frequency Array

Approach:
- Build frequency arrays for p and the first window of s.
- Compare the arrays and record index 0 if they match.
- Slide a window of length len(p) through s.
- Add the incoming character and remove the outgoing character.
- Whenever the frequency arrays match, record the window's
  starting index as an anagram occurrence.

Time Complexity: O(n + m)
Space Complexity: O(1)
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n = len(s)
        m = len(p)
        res = []

        if m > n:
            return []

        p_count = [0] * 26
        win_freq = [0] * 26

        for i in range(m):
            p_count[ord(p[i]) - ord('a')] += 1
            win_freq[ord(s[i]) - ord('a')] += 1

        if p_count == win_freq:
            res.append(0)

        for right in range(m, n):
            incoming = ord(s[right]) - ord('a')
            outgoing = ord(s[right - m]) - ord('a')

            win_freq[incoming] += 1
            win_freq[outgoing] -= 1

            if p_count == win_freq:
                res.append(right - m + 1)

        return res
