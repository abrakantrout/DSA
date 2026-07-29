"""
Problem: Product of Array Except Self
LeetCode: 238
Difficulty: Medium

Topic:
- Array
- Prefix Product
- Suffix Product

Approach:
- Store the product of all elements to the left of each index.
- Traverse from right to left while maintaining a running suffix product.
- Multiply the prefix product with the suffix product for each index.
- This avoids division and uses constant extra space (excluding the output array).

Time Complexity: O(n)
Space Complexity: O(1) (excluding the output array)
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        right = 1

        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer