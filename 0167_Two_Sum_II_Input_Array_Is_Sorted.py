"""
Problem: Two Sum II - Input Array Is Sorted
LeetCode: 167
Difficulty: Medium

Topic:
- Array
- Two Pointers

Approach:
- Use two pointers, one at the beginning and one at the end.
- If the current sum is too large, move the right pointer left.
- If the current sum is too small, move the left pointer right.
- When the sum equals the target, return the 1-indexed positions.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curr_sum = numbers[l] + numbers[r]

            if curr_sum > target:
                r -= 1

            elif curr_sum < target:
                l += 1

            else:
                return [l + 1, r + 1]