"""
Problem: Combinations
LeetCode: 77
Difficulty: Medium

Topic:
- Backtracking
- Recursion
- Combinations

Approach:
- Build combinations by choosing numbers from start to n.
- Once k numbers are selected, store the current combination.
- Start the next recursive call from i + 1 so the same number
  cannot be selected again.
- Backtrack by removing the last selected number.

Time Complexity: O(C(n, k) * k)
Space Complexity: O(k) auxiliary space (excluding the output)
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def solution(start, curr, result):
            if len(curr) == k:
                result.append(curr.copy())
                return

            for i in range(start, n + 1):
                curr.append(i)

                solution(i + 1, curr, result)

                curr.pop()

        solution(1, [], result)

        return result