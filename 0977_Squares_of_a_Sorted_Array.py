
"""
Problem: Squares of a Sorted Array
LeetCode: 977
Difficulty: Easy

Topic:
- Arrays
- Two Pointers

Approach:
- Use two pointers at the beginning and end of the sorted array.
- Compare the absolute values at both pointers.
- Square the larger absolute value and insert it at the front of the deque.
- Move the pointer corresponding to the selected element inward.
- Continue until all elements are processed.
- Convert the deque into a list and return it.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res = deque()
        l = 0
        r = len(nums) - 1

        while l <= r:
            if abs(nums[r]) > abs(nums[l]):
                res.appendleft(nums[r] ** 2)
                r -= 1

            else:
                res.appendleft(nums[l] ** 2)
                l += 1

        return list(res)
