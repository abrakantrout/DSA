"""
Problem: Contains Duplicate
LeetCode: 217
Difficulty: Easy

Topic:
- Array
- Hash Set

Approach:
- Use a hash set to keep track of elements seen so far.
- If the current element already exists in the set, return True.
- Otherwise, add it to the set.
- If the traversal finishes without duplicates, return False.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False