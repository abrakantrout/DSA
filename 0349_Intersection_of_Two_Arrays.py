
"""
Problem: Intersection of Two Arrays
LeetCode: 349
Difficulty: Easy

Topic:
- Arrays
- Hashing
- Sets

Approach:
- Convert nums1 into a set for efficient membership checking.
- Create an empty set to store the common elements.
- Iterate through nums2.
- If an element exists in the first set, add it to the result set.
- Using a set automatically handles duplicates.
- Convert the result set into a list and return it.

Time Complexity: O(n + m)
Space Complexity: O(n + m)

Where:
- n = length of nums1
- m = length of nums2
"""

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hs = set(nums1)
        ans = set()

        for num in nums2:
            if num in hs:
                ans.add(num)

        return list(ans)
