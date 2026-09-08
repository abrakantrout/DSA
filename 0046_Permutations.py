"""
Problem: Permutations
LeetCode: 46
Difficulty: Medium

Topic:
- Backtracking
- Recursion
- Arrays

Approach:
- Build the permutation one element at a time.
- Use a boolean array to track which elements have already
  been used in the current permutation.
- For each unused element:
  1. Choose the element.
  2. Mark it as used.
  3. Recursively continue building the permutation.
  4. Unmark it and remove it from the current permutation.
- When the current permutation contains all elements, add a copy
  to the result.

Time Complexity: O(n * n!)

Space Complexity: O(n)

The result contains n! permutations, and copying each permutation
takes O(n) time.
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        used = [False] * len(nums)

        def backtrack(current):
            if len(current) == len(nums):
                result.append(current.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                current.append(nums[i])
                used[i] = True

                backtrack(current)

                used[i] = False
                current.pop()

        backtrack(current)

        return result