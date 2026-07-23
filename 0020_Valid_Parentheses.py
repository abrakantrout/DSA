"""
Problem: Valid Parentheses
LeetCode: 20
Difficulty: Easy

Topic:
- String
- Stack

Approach:
- Use a stack to keep track of opening brackets.
- Push opening brackets onto the stack.
- For every closing bracket, check whether it matches the top of the stack.
- If it doesn't match or the stack is empty, return False.
- At the end, the stack should be empty for the string to be valid.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack:
                    return False

                elif stack[-1] != pairs[ch]:
                    return False

                stack.pop()

        return len(stack) == 0