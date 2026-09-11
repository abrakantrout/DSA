"""
Problem: Combination Sum
LeetCode: 39
Difficulty: Medium

Topic:
- Backtracking
- Recursion
- Arrays

Approach:
- Starting from a given index, try each candidate.
- Add the candidate to the current combination.
- Recursively continue using the same index because each candidate
  can be used unlimited times.
- If the target is reached, store the current combination.
- If the total exceeds the target, stop exploring that path.
- Backtrack by removing the last chosen candidate.

Time Complexity: O(n^(target/min_candidate)) approximately
Space Complexity: O(target/min_candidate) excluding the output
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, current, total):
            if total == target:
                result.append(current.copy())
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])

                backtrack(i, current, total + candidates[i])

                current.pop()

        backtrack(0, [], 0)

        return result