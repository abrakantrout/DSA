
"""
Problem: Search Insert Position
LeetCode: 35
Difficulty: Easy

Topic:
- Arrays
- Binary Search

Approach:
- Initialize low and high to represent the search range.
- Calculate the middle index in each iteration.
- If nums[mid] is smaller than the target, search the right half.
- Otherwise, search the left half, including when nums[mid] equals target.
- When the search range becomes empty, low represents the correct
  insertion position.
- Return low.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] < target:
                low = mid + 1

            elif nums[mid] >= target:
                high = mid - 1

        return low
