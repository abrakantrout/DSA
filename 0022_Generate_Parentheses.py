"""
Problem: Generate Parentheses
LeetCode: 22
Difficulty: Medium

Topic:
- Backtracking
- Recursion
- Strings

Approach:
- Build the parenthesis string one character at a time.
- Add '(' while fewer than n opening parentheses have been used.
- Add ')' only when the number of closing parentheses is less than
  the number of opening parentheses.
- This guarantees that every generated string is valid.
- When the string reaches length 2*n, add it to the result.

Time Complexity: O(4^n / sqrt(n))
Space Complexity: O(n) auxiliary space (excluding the output)
"""

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(curr, open, close):
            if len(curr) == 2 * n:
                res.append("".join(curr))
                return

            if open < n:
                curr.append('(')
                backtrack(curr, open + 1, close)
                curr.pop()

            if close < open:
                curr.append(')')
                backtrack(curr, open, close + 1)
                curr.pop()

        backtrack([], 0, 0)

        return res