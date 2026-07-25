"""
Problem: Maximum Subarray
LeetCode: 53
Difficulty: Medium

Topic:
- Array
- Dynamic Programming
- Kadane's Algorithm

Approach:
- Traverse the array while maintaining the current subarray sum.
- Update the maximum subarray sum found so far.
- If the current sum becomes negative, reset it to zero since it cannot
  contribute to a larger sum ahead.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = nums[0]

        for num in nums:
            cur_sum += num
            max_sum = max(max_sum, cur_sum)

            if cur_sum < 0:
                cur_sum = 0

        return max_sum