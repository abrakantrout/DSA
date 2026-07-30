"""
Problem: Decode String
LeetCode: 394
Difficulty: Medium

Topic:
- String
- Stack

Approach:
- Traverse the string character by character.
- Push characters onto the stack until a closing bracket is encountered.
- When ']' is found:
  - Pop characters to build the encoded substring.
  - Pop the matching '['.
  - Pop the digits representing the repeat count.
  - Repeat the substring and push it back onto the stack.
- Join the stack to obtain the decoded string.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for item in s:
            if item != ']':
                stack.append(item)
            else:
                current = ""

                while stack[-1] != '[':
                    current = stack.pop() + current

                stack.pop()

                num = ""

                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                stack.append(int(num) * current)

        return "".join(stack)