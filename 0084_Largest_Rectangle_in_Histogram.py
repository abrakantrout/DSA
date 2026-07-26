"""
Problem: Largest Rectangle in Histogram
LeetCode: 84
Difficulty: Hard

Topic:
- Array
- Stack
- Monotonic Stack

Approach:
- Use a monotonic increasing stack to store indices of bars.
- When a shorter bar is encountered, pop taller bars from the stack.
- For each popped bar, calculate the largest rectangle where it is the
  limiting height.
- Append a dummy bar of height 0 to process any remaining bars in the stack.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        n = len(heights)

        stack = []
        max_area = 0

        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = width * height
                max_area = max(max_area, area)

            stack.append(i)

        heights.pop()
        return max_area