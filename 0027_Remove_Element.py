
"""
Problem: Remove Element
LeetCode: 27
Difficulty: Easy

Topic:
- Arrays
- Two Pointers
- In-Place Modification

Approach:
- Use l to track the position where the next valid element should be placed.
- Iterate through the array using r.
- If nums[r] is not equal to val, copy it to nums[l] and increment l.
- Return l, which represents the number of elements not equal to val.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        l = 0

        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1

        return l
