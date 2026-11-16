
"""
Problem: Sort Characters By Frequency
LeetCode: 451
Difficulty: Medium

Topic:
- Strings
- Hashing
- Sorting

Approach:
- Use a dictionary to count the frequency of each character.
- Sort the dictionary items in descending order based on frequency.
- Iterate through the sorted items.
- Multiply each character by its frequency and append it to the result.
- Return the final string.

Time Complexity: O(n + k log k)
Space Complexity: O(n + k)

Where:
- n = length of the string
- k = number of distinct characters
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

        ans = ""

        for char, count in sorted_freq.items():
            ans += char * count

        return ans
