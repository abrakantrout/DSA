"""
Problem: Binary Tree Right Side View
LeetCode: 199
Difficulty: Medium

Topic:
- Binary Tree
- Breadth-First Search
- Queue
- Level Order Traversal

Approach:
- Perform a level-order traversal using a queue.
- Process each level separately.
- The last node processed at each level is the node visible
  from the right side.
- Add that node's value to the result.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(
        self,
        root: Optional[TreeNode]
    ) -> List[int]:

        if root is None:
            return []

        queue = deque([root])
        result = []

        while queue:
            length = len(queue)

            for i in range(length):
                node = queue.popleft()

                if i == length - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return result