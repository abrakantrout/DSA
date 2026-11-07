
"""
Problem: Search in Rotated Sorted Array
LeetCode: 33
Difficulty: Medium

Topic:
- Arrays
- Binary Search
- Modified Binary Search

Approach:
- Use binary search to search in the rotated sorted array.
- Calculate mid and check whether the target is found.
- Determine which half of the current search range is sorted.
- If the left half is sorted:
  - Check whether the target lies within that half.
  - If yes, search the left half; otherwise, search the right half.
- If the right half is sorted:
  - Check whether the target lies within that half.
  - If yes, search the right half; otherwise, search the left half.
- Continue until the target is found or the search range becomes empty.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            elif nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
