"""
Problem: Reorganize String
LeetCode: 767
Difficulty: Medium

Topic:
- Heaps
- Greedy
- Hashing
- Strings

Approach:
- Count the frequency of each character.
- Use a max heap to always choose the most frequent
  character that is currently available.
- Temporarily hold the previously used character so that
  the same character cannot be selected consecutively.
- After selecting another character, put the held character
  back into the heap.
- If a character remains held at the end, it cannot be placed
  without creating adjacent duplicates, so return "".

Time Complexity: O(n log k)
Space Complexity: O(k)
"""

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        heap = []

        for char, count in freq.items():
            heapq.heappush(heap, (-count, char))

        result = []
        hold = None

        while heap:
            count, char = heapq.heappop(heap)

            result.append(char)
            count += 1

            if hold:
                heapq.heappush(heap, hold)
                hold = None

            if count < 0:
                hold = (count, char)

        if hold:
            return ""

        return "".join(result)