
"""
Problem: Max Consecutive Ones III
LeetCode: 1004
Difficulty: Medium

Topic:
- Arrays
- Sliding Window
- Two Pointers

Approach:
- Maintain a window containing at most k zeros.
- Expand the window by moving the right pointer.
- Count zeros entering the window.
- If the number of zeros exceeds k, shrink the window
  from the left until it becomes valid.
- Track the maximum valid window length.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        zero_count = 0
        length = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[l] == 0:
                    zero_count -= 1

                l += 1

            curr_len = r - l + 1
            length = max(curr_len, length)

        return length
