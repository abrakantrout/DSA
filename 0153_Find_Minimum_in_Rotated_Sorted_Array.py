
"""
Problem: Find Minimum in Rotated Sorted Array
LeetCode: 153
Difficulty: Medium

Topic:
- Arrays
- Binary Search
- Modified Binary Search

Approach:
- Use binary search to find the minimum element.
- Compare nums[mid] with nums[high].
- If nums[mid] > nums[high], the minimum must be in the right half.
  Move low to mid + 1.
- Otherwise, the minimum is at mid or in the left half.
  Move high to mid.
- Continue until low and high point to the same index.
- Return nums[low].

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1

            elif nums[mid] <= nums[high]:
                high = mid

        return nums[low]
