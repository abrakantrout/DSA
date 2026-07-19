"""
Problem: Best Time to Buy and Sell Stock
LeetCode: 121
Difficulty: Easy

Topic:
- Array
- Two Pointers

Approach:
- Use two pointers:
  - l = buying day
  - r = selling day
- If current selling price is greater than buying price,
  calculate profit and update maximum profit.
- If current selling price is smaller,
  move the buying pointer to the current day.
- Continue until the end of the array.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxp = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxp = max(maxp, profit)
            else:
                l = r

            r += 1

        return maxp