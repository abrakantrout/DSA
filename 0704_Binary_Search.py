
"""
Problem: Binary Search
LeetCode: 704
Difficulty: Easy

Topic:
- Arrays
- Binary Search

Approach:
- Initialize low and high pointers to represent the search range.
- Calculate the middle index in each iteration.
- If nums[mid] equals the target, return mid.
- If nums[mid] is smaller than the target, search the right half.
- Otherwise, search the left half.
- Continue until the target is found or the search range becomes empty.
- Return -1 if the target is not present.

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

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return -1
