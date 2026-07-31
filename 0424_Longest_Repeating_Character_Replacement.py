"""
Problem: Longest Repeating Character Replacement
LeetCode: 424
Difficulty: Medium

Topic:
- String
- Hash Map
- Sliding Window

Approach:
- Use a variable-size sliding window.
- Maintain the frequency of characters within the current window.
- Keep track of the maximum frequency of any character in the window.
- If the number of characters to replace exceeds k, shrink the window.
- Track the maximum valid window size throughout the traversal.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        mfreq = 0
        ans = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1

            mfreq = max(mfreq, freq[s[r]])

            while (r - l + 1) - mfreq > k:
                freq[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans