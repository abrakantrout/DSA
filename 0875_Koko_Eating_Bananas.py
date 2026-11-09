
"""
Problem: Koko Eating Bananas
LeetCode: 875
Difficulty: Medium

Topic:
- Arrays
- Binary Search
- Binary Search on Answer

Approach:
- Search for the minimum valid eating speed.
- Set low = 1 and high = max(piles).
- For each mid, calculate the total hours required to finish all piles.
- Use ceiling division (pile + mid - 1) // mid to calculate
  the hours needed for each pile.
- If the total hours are within h:
  - The current speed is valid.
  - Store it as the answer and search for a smaller speed.
- Otherwise, increase the eating speed.
- Return the minimum valid speed.

Time Complexity: O(n log m)
Space Complexity: O(1)

Where:
- n = number of piles
- m = maximum pile size
"""

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            hours = 0

            for pile in piles:
                hours += (pile + mid - 1) // mid

            if hours <= h:
                high = mid - 1
                ans = mid

            else:
                low = mid + 1

        return ans
