
"""
Problem: Fruit Into Baskets
LeetCode: 904
Difficulty: Medium

Topic:
- Arrays
- Sliding Window
- Hash Map

Approach:
- Maintain a frequency dictionary for the fruits in the current window.
- Expand the window by moving the right pointer and updating frequencies.
- If the window contains more than two distinct fruit types, shrink it
  from the left until only two types remain.
- Track the maximum valid window length.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        freq = {}
        max_count = 0
        l = 0

        for r in range(len(fruits)):
            fr = fruits[r]
            freq[fr] = freq.get(fr, 0) + 1

            while len(freq) > 2:
                freq[fruits[l]] -= 1
                if freq[fruits[l]] == 0:
                    del freq[fruits[l]]
                l += 1

            max_count = max((r - l + 1), max_count)

        return max_count
