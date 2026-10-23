
"""
Problem: Move Zeroes
LeetCode: 283
Difficulty: Easy

Topic:
- Arrays
- Two Pointers
- In-Place Modification

Approach:
- Use l to track the position where the next non-zero element belongs.
- Iterate through the array using r.
- Whenever nums[r] is non-zero, swap nums[l] and nums[r].
- Increment l to move to the next position for a non-zero element.
- This preserves the relative order of non-zero elements and moves
  all zeroes to the end.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0

        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
