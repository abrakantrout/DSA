# Problem: Palindrome Partitioning
# LeetCode: 131
# Difficulty: Medium
# Topic: Backtracking, Recursion, Palindrome
# Approach: Try every possible substring starting at the current index.
#           If the substring is a palindrome, choose it and recursively
#           partition the remaining string. Backtrack by removing the choice.
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n) auxiliary space (excluding the output)


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(start, current):
            if start == len(s):
                result.append(current.copy())
                return

            for i in range(start, len(s)):
                if s[start:i+1] == s[start:i+1][::-1]:
                    current.append(s[start:i+1])

                    backtrack(i + 1, current)

                    current.pop()

        backtrack(0, [])

        return result