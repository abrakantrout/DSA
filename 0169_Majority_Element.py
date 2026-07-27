"""
Problem: Majority Element
LeetCode: 169
Difficulty: Easy

Topic:
- Array
- Hash Map

Approach:
- Count the frequency of each element using a hash map.
- Traverse the frequency map to find the element with the highest count.
- Return the element with the maximum frequency.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        max_freq = 0
        freq_num = 0

        for num, count in freq.items():
            if count > max_freq:
                max_freq = count
                freq_num = num

        return freq_num