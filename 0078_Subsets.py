"""
Problem: Subsets
LeetCode: 78
Difficulty: Medium

Topic:
- Backtracking
- Recursion
- Arrays

Approach:
- For each element, make two choices:
  1. Include the element in the current subset.
  2. Exclude the element from the current subset.
- Recursively explore both choices.
- When all elements have been considered, add a copy of the
  current subset to the result.

Time Complexity: O(n * 2^n)
Space Complexity: O(n)

The result itself contains 2^n subsets, and copying each subset
takes up to O(n) time.
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []

        def backtrack(index, curr, result):
            if index == len(nums):
                result.append(curr.copy())
                return

            curr.append(nums[index])

            backtrack(index + 1, curr, result)

            curr.pop()

            backtrack(index + 1, curr, result)

        backtrack(0, curr, result)

        return result