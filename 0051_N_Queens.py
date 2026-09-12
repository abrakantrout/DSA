"""
Problem: N-Queens
LeetCode: 51
Difficulty: Hard

Topic:
- Backtracking
- Recursion
- Sets
- Matrix

Approach:
- Place exactly one queen in each row.
- Track occupied columns using a set.
- Track both diagonal directions using:
    row - col
    row + col
- If a position is safe, place the queen and recursively move
  to the next row.
- After returning, remove the queen and undo all tracking changes.

Time Complexity: O(N!)
Space Complexity: O(N^2)
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)

        return result