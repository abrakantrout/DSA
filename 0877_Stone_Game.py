"""
Problem: Stone Game
LeetCode: 877
Difficulty: Medium

Topic:
- Dynamic Programming
- Game Theory

Approach:
- The number of piles is guaranteed to be even.
- Alex can always choose a strategy that guarantees taking either
  all even-indexed piles or all odd-indexed piles.
- Since the total number of stones is odd, one of these two groups
  must contain more stones than the other.
- Therefore, Alex can always guarantee a win.

Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True