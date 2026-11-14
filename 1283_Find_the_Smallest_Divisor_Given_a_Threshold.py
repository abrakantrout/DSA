
"""
Problem: Find the Smallest Divisor Given a Threshold
LeetCode: 1283
Difficulty: Medium

Topic:
- Arrays
- Binary Search
- Binary Search on Answer

Approach:
- Search for the smallest divisor that makes the sum of rounded-up
  division results less than or equal to the threshold.
- Set low = 1 and high = max(nums).
- For each mid, calculate the total using ceiling division:
  (num + mid - 1) // mid.
- If the total is within the threshold:
  - The current divisor is valid.
  - Store it as the answer and search for a smaller divisor.
- Otherwise, increase the divisor.
- Return the smallest valid divisor.

Time Complexity: O(n log m)
Space Complexity: O(1)

Where:
- n = number of elements in nums
- m = maximum element in nums
"""

class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            total = 0

            for num in nums:
                total += (num + mid - 1) // mid

            if total <= threshold:
                ans = mid
                high = mid - 1

            else:
                low = mid + 1

        return ans
