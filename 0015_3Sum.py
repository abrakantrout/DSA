"""
Problem: 3Sum
LeetCode: 15
Difficulty: Medium

Topic:
- Array
- Sorting
- Two Pointers

Approach:
- Sort the array first.
- Fix one element and use two pointers to find two other
  elements whose sum completes the target of zero.
- Move the left pointer when the sum is too small.
- Move the right pointer when the sum is too large.
- Skip duplicate values to avoid duplicate triplets.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        curr = 0

        while curr < len(nums) - 2:
            if curr > 0 and nums[curr] == nums[curr - 1]:
                curr += 1
                continue

            left = curr + 1
            right = len(nums) - 1

            while left < right:
                ans = nums[curr] + nums[left] + nums[right]

                if ans == 0:
                    res.append([
                        nums[curr],
                        nums[left],
                        nums[right]
                    ])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif ans > 0:
                    right -= 1

                else:
                    left += 1

            curr += 1

        return res