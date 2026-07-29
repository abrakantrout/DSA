"""
Problem: Implement Queue using Stacks
LeetCode: 232
Difficulty: Easy

Topic:
- Stack
- Queue
- Design

Approach:
- Use two stacks:
  - input_stack stores newly added elements.
  - output_stack provides queue order.
- When removing or peeking, transfer elements from input_stack to
  output_stack only if output_stack is empty.
- This preserves FIFO order while using only stack operations.

Time Complexity:
- push: O(1)
- pop: Amortized O(1)
- peek: Amortized O(1)
- empty: O(1)

Space Complexity: O(n)
"""

class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output_stack.pop()

    def peek(self) -> int:
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

        return self.output_stack[-1]

    def empty(self) -> bool:
        return not self.input_stack and not self.output_stack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()