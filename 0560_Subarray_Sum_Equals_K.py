
"""
Problem: Subarray Sum Equals K
LeetCode: 560
Difficulty: Medium

Topic:
- Arrays
- Hashing
- Prefix Sum

Approach:
- Maintain a running prefix sum while iterating through the array.
- Use a frequency dictionary to store how many times each prefix sum
  has occurred.
- Initialize freq = {0: 1} to handle subarrays starting at index 0.
- For each element:
  - Update the current prefix sum.
  - Calculate the required previous prefix sum: cur_sum - k.
  - If it exists in the dictionary, add its frequency to count.
  - Update the frequency of the current prefix sum.
- Return the total number of valid subarrays.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0: 1}
        cur_sum = 0
        count = 0

        for num in nums:
            cur_sum += num

            required = cur_sum - k
            if required in freq:
                count += freq[required]

            freq[cur_sum] = freq.get(cur_sum, 0) + 1

        return count
