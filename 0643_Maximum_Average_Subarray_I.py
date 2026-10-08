"""
Problem: Maximum Average Subarray I
LeetCode: 643
Difficulty: Easy

Topic:
- Arrays
- Sliding Window

Approach:
- Maintain a window of exactly k elements.
- Calculate the sum of the first window.
- Slide the window by removing the leftmost element
  and adding the new rightmost element.
- Track the maximum window sum.
- Divide the maximum sum by k to get the maximum average.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = 0

        for i in range(k):
            window_sum += nums[i]

        left = 0
        max_sum = window_sum

        for right in range(k, len(nums)):
            window_sum = window_sum - nums[left] + nums[right]
            max_sum = max(max_sum, window_sum)
            left += 1

        return max_sum / k