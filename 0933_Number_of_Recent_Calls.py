"""
Problem: Number of Recent Calls
LeetCode: 933
Difficulty: Easy

Topic:
- Queue
- Design
- Sliding Window

Approach:
- Use a queue to store the timestamps of recent requests.
- Add each new request to the queue.
- Remove timestamps that are older than 3000 milliseconds from the current request.
- The remaining elements in the queue represent all recent requests.

Time Complexity: O(1) Amortized
Space Complexity: O(n)
"""

from collections import deque

class RecentCounter:

    def __init__(self):
        self.RecentCounter = deque()

    def ping(self, t: int) -> int:
        self.RecentCounter.append(t)

        while self.RecentCounter[0] < t - 3000:
            self.RecentCounter.popleft()

        return len(self.RecentCounter)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)