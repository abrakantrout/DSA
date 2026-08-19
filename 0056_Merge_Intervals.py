"""
Problem: Merge Intervals
LeetCode: 56
Difficulty: Medium

Topic:
- Array
- Sorting
- Intervals

Approach:
- Sort the intervals by their starting values.
- Compare each interval with the current merged interval.
- If the intervals do not overlap, add the current interval to the result
  and start processing the next interval.
- If they overlap, merge them by taking the earliest start and latest end.
- Add the final interval to the result.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        result = []
        curr = intervals[0]

        for i in range(len(intervals) - 1):
            first = curr
            second = intervals[i + 1]

            if first[-1] < second[0]:
                result.append(first)
                curr = second
            else:
                curr = [
                    min(first[0], second[0]),
                    max(first[-1], second[-1])
                ]

        result.append(curr)

        return result