"""
Problem: Daily Temperatures
LeetCode: 739
Difficulty: Medium

Topic:
- Array
- Stack
- Monotonic Stack

Approach:
- Use a monotonic decreasing stack to store indices of temperatures.
- For each new temperature, compare it with the temperature at the index
  on the top of the stack.
- While the current temperature is warmer, pop indices from the stack
  and calculate the number of days waited.
- Push the current index onto the stack.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                result[prev] = i - prev

            stack.append(i)

        return result