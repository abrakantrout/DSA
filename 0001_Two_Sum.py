"""
Problem: Two Sum
LeetCode: 1
Difficulty: Easy

Topic:
- Array
- Hash Map

Approach:
- Use a hash map to store previously seen numbers and their indices.
- For each number, calculate the complement needed to reach the target.
- If the complement already exists in the hash map, return both indices.
- Otherwise, store the current number and continue.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in prevMap:
                return [prevMap[diff], i]

            prevMap[n] = i