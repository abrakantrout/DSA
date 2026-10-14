
"""
Problem: Longest Substring Without Repeating Characters
LeetCode: 3
Difficulty: Medium

Topic:
- Strings
- Sliding Window
- Hash Set
- Two Pointers

Approach:
- Maintain a window containing only unique characters.
- Use a set to track the characters currently in the window.
- Expand the window by moving the right pointer.
- If a duplicate appears, shrink the window from the left
  until the duplicate is removed.
- Update the maximum window length after each expansion.

Time Complexity: O(n)
Space Complexity: O(min(n, charset))
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        count = 1
        l = 0
        seen = {s[0]}

        for r in range(1, len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])

            curr_count = r - l + 1
            count = max(curr_count, count)

        return count
