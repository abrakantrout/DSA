"""
Problem: Sort Colors
LeetCode: 75
Difficulty: Medium

Topic:
- Two Pointers
- Arrays
- Dutch National Flag

Approach:
- Use three pointers:
    low  -> boundary for 0s
    mid  -> current element being examined
    high -> boundary for 2s
- If nums[mid] is 0, swap it with low and move both low and mid.
- If nums[mid] is 1, it is already in the correct region, so move mid.
- If nums[mid] is 2, swap it with high and move high.
  Do not move mid because the swapped element still needs to be checked.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1