
"""
Problem: Merge Sorted Array
LeetCode: 88
Difficulty: Easy

Topic:
- Arrays
- Two Pointers
- In-Place Modification

Approach:
- Use i and j to point to the last valid elements of nums1 and nums2.
- Use k to point to the last position of nums1.
- Compare the elements from the end and place the larger element at nums1[k].
- Move the corresponding pointer backward after each placement.
- If elements remain in nums2, copy them into nums1.
- Remaining elements in nums1 are already in their correct positions.

Time Complexity: O(m + n)
Space Complexity: O(1)
"""

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1

            elif nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1

            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
