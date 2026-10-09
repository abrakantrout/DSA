
"""
Problem: Minimum Size Subarray Sum
LeetCode: 209
Difficulty: Medium

Topic:
- Arrays
- Sliding Window
- Two Pointers

Approach:
- Expand the window by moving the right pointer.
- Add each new element to the window sum.
- While the sum is at least the target, update the minimum length
  and shrink the window from the left.
- Return 0 if no valid subarray exists.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        window_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                length = right - left + 1
                min_len = min(min_len, length)

                window_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len