"""
Problem: Maximum Product of Two Elements in an Array
LeetCode: 1464
Difficulty: Easy

Topic:
- Array

Approach:
- Traverse the array once while keeping track of the largest and
  second largest elements.
- Update the two maximum values as larger elements are encountered.
- Compute (largest - 1) × (second largest - 1).

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = 0
        max2 = 0

        for num in nums:
            if num >= max1:
                max2 = max1
                max1 = num
            elif num >= max2:
                max2 = num

        return (max1 - 1) * (max2 - 1)