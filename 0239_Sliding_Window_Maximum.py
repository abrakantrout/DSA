"""
Problem: Sliding Window Maximum
LeetCode: 239
Difficulty: Hard

Topic:
- Arrays
- Sliding Window
- Monotonic Deque

Approach:
- Store indices in a deque, maintaining decreasing order of values.
- Remove indices that have fallen outside the current window.
- Remove indices from the back while their values are less than
  or equal to the current value, since they cannot be the maximum
  for this or any future window containing the current element.
- Append the current index.
- Once the first complete window is formed, append the value at
  the front of the deque to the result.

Time Complexity: O(n)
Space Complexity: O(k)
"""

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        dq = deque()

        for r in range(len(nums)):
            while dq and dq[0] <= r - k:
                dq.popleft()

            while dq and nums[dq[-1]] <= nums[r]:
                dq.pop()

            dq.append(r)

            if r >= k - 1:
                res.append(nums[dq[0]])

        return res
