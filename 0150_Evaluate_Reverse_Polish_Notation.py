"""
Problem: Evaluate Reverse Polish Notation
LeetCode: 150
Difficulty: Medium

Topic:
- Stack
- Expression Evaluation

Approach:
- Use a stack to store operands.
- When a number is encountered, push it onto the stack.
- When an operator is encountered, pop the two most recent operands.
- Apply the operator and push the result back onto the stack.
- The final value remaining in the stack is the answer.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char in "+-*/":
                val1 = stack.pop()
                val2 = stack.pop()

                if char == '+':
                    stack.append(val1 + val2)

                elif char == '-':
                    stack.append(val2 - val1)

                elif char == '*':
                    stack.append(val1 * val2)

                elif char == '/':
                    stack.append(int(val2 / val1))

            else:
                stack.append(int(char))

        return stack.pop()