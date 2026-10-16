
"""
Problem: Contains Duplicate II
LeetCode: 219
Difficulty: Easy

Topic:
- Arrays
- Sliding Window
- Hash Set

Approach:
- Maintain a set containing the previous k elements.
- Before adding the current element, check whether it is
  already in the set.
- If it is, a duplicate exists within distance k.
- Remove the element that falls outside the window.

Time Complexity: O(n)
Space Complexity: O(min(n, k))
"""

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = set()
        left = 0

        for right in range(len(nums)):
            if nums[right] in seen:
                return True

            seen.add(nums[right])

            if right - left >= k:
                seen.remove(nums[left])
                left += 1

        return False
