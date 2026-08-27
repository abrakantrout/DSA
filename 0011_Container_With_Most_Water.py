"""
Problem: Container With Most Water
LeetCode: 11
Difficulty: Medium

Topic:
- Array
- Two Pointers

Approach:
- Start with two pointers at the left and right ends of the array.
- Calculate the area formed by the two heights.
- Move the pointer with the smaller height because the shorter
  height limits the maximum possible area.
- Continue until the two pointers meet.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0

        while left < right:
            ans = (right - left) * min(height[left], height[right])
            res = max(res, ans)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res