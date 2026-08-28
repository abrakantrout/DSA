"""
Problem: Longest Consecutive Sequence
LeetCode: 128
Difficulty: Medium

Topic:
- Array
- Hash Set

Approach:
- Store all numbers in a set for O(1) average lookup.
- Only start counting when the current number is the beginning
  of a consecutive sequence, meaning num - 1 is not in the set.
- Continue checking num + 1, num + 2, etc. to find the sequence length.
- Track the longest sequence found.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        max_count = 0

        for num in hs:
            curr_count = 0

            if num - 1 not in hs:
                curr_count += 1
                curr = num

                while curr + 1 in hs:
                    curr_count += 1
                    curr += 1

            max_count = max(max_count, curr_count)

        return max_count