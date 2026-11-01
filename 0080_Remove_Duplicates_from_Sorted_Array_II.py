
"""
Problem: Remove Duplicates from Sorted Array II
LeetCode: 80
Difficulty: Medium

Topic:
- Arrays
- Two Pointers
- In-Place Modification

Approach:
- Since the array is sorted, duplicates appear consecutively.
- Allow the first two elements to remain unchanged.
- Use l to track the position where the next valid element should be placed.
- Iterate through the array starting from index 2 using r.
- If nums[r] is different from nums[l - 2], it means the element
  can be included without allowing more than two occurrences.
- Place the element at nums[l] and increment l.
- Return l as the length of the modified array.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 2

        for r in range(2, len(nums)):
            if nums[r] != nums[l - 2]:
                nums[l] = nums[r]
                l += 1

        return l
