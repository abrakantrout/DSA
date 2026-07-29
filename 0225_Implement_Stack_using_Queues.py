"""
Problem: Implement Stack using Queues
LeetCode: 225
Difficulty: Easy

Topic:
- Stack
- Design

Approach:
- Use a Python list to simulate stack operations.
- Push elements to the end of the list.
- Pop the last element for LIFO behavior.
- Access the last element for the top operation.
- Check if the list is empty.

Time Complexity:
- push: O(1)
- pop: O(1)
- top: O(1)
- empty: O(1)

Space Complexity: O(n)
"""

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()