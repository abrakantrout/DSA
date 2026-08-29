"""
Problem: Fibonacci Number
LeetCode: 509
Difficulty: Easy

Topic:
- Recursion
- Dynamic Programming

Approach:
- Use the recursive definition of the Fibonacci sequence.
- Base cases:
  - fib(0) = 0
  - fib(1) = 1
- For n > 1, calculate fib(n) using:
  fib(n) = fib(n - 1) + fib(n - 2).

Time Complexity: O(2^n)
Space Complexity: O(n)
"""

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        elif n == 1:
            return 1

        elif n > 1:
            return self.fib(n - 1) + self.fib(n - 2)