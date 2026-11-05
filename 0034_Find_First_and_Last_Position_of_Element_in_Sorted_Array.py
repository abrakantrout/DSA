
"""
Problem: Find First and Last Position of Element in Sorted Array
LeetCode: 34
Difficulty: Medium

Topic:
- Arrays
- Binary Search
- Boundary Search

Approach:
- Use two separate binary searches to find the target's boundaries.
- findFirst():
  - If nums[mid] is smaller than the target, search the right half.
  - Otherwise, continue searching the left half.
  - After the loop, low represents the first possible occurrence.
- findLast():
  - If nums[mid] is greater than the target, search the left half.
  - Otherwise, continue searching the right half.
  - After the loop, high represents the last possible occurrence.
- Return both positions. If the target is absent, return [-1, -1].

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findFirst():
            low, high = 0, len(nums) - 1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            if low < len(nums) and nums[low] == target:
                return low

            return -1

        def findLast():
            low, high = 0, len(nums) - 1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1

            if high >= 0 and nums[high] == target:
                return high

            return -1

        return [findFirst(), findLast()]
