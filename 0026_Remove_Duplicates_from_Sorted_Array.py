"""
Problem: Remove Duplicates from Sorted Array
LeetCode: 26
Difficulty: Easy

Topic:
- Array
- Two Pointers

Approach:
- Use two pointers:
  - 'write' keeps track of the position for the next unique element.
  - 'read' scans through the array.
- When a new unique element is found, move the write pointer forward
  and overwrite the next position with that element.
- Return the number of unique elements.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0

        for read in range(1, len(nums)):
            if nums[read] != nums[write]:
                write += 1
                nums[write] = nums[read]

        return write + 1