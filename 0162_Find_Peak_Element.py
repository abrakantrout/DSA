
"""
Problem: Find Peak Element
LeetCode: 162
Difficulty: Medium

Topic:
- Arrays
- Binary Search
- Modified Binary Search

Approach:
- Use binary search to find a peak element.
- Compare nums[mid] with nums[mid + 1].
- If nums[mid] < nums[mid + 1], the array is increasing
  toward the right, so a peak must exist on the right side.
  Move low to mid + 1.
- Otherwise, a peak exists at mid or somewhere on the left.
  Move high to mid.
- Continue until low and high point to the same index.
- Return that index.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] < nums[mid + 1]:
                low = mid + 1

            else:
                high = mid

        return low
