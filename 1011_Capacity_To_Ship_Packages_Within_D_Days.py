
"""
Problem: Capacity To Ship Packages Within D Days
LeetCode: 1011
Difficulty: Medium

Topic:
- Arrays
- Binary Search
- Binary Search on Answer

Approach:
- Search for the minimum ship capacity that allows all packages
  to be delivered within the given number of days.
- Set low = max(weights), since the ship must carry at least
  the heaviest package.
- Set high = sum(weights), since this capacity can ship everything
  in one day.
- For each mid, simulate shipping packages in their original order.
- If adding a package exceeds the capacity:
  - Start a new day.
  - Set the current load to that package's weight.
- Otherwise, add the package to the current day's load.
- If the required days exceed the given days, increase capacity.
- Otherwise, store the capacity and search for a smaller one.
- Return the minimum valid capacity.

Time Complexity: O(n log(sum(weights) - max(weights) + 1))
Space Complexity: O(1)
"""

class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            cur_load = 0
            req_days = 1

            for weight in weights:
                if cur_load + weight > mid:
                    req_days += 1
                    cur_load = weight
                else:
                    cur_load += weight

            if req_days > days:
                low = mid + 1

            else:
                ans = mid
                high = mid - 1

        return ans
