"""
Problem: Valid Anagram
LeetCode: 242
Difficulty: Easy

Topic:
- String
- Hash Map

Approach:
- Count the frequency of each character in both strings.
- Compare the two frequency maps.
- If they are equal, the strings are anagrams.

Time Complexity: O(n + m)
Space Complexity: O(k)

where:
- n = length of s
- m = length of t
- k = number of unique characters
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        freq_t = {}

        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1

        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1

        return freq_s == freq_t