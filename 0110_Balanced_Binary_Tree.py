"""
Problem: Balanced Binary Tree
LeetCode: 110
Difficulty: Easy

Topic:
- Binary Tree
- Depth-First Search
- Recursion

Approach:
- Recursively calculate the height of each subtree.
- For every node, check:
  - Whether the left subtree is balanced.
  - Whether the right subtree is balanced.
  - Whether the difference between the left and right subtree heights
    is at most 1.
- Return both the balance status and height from each recursive call.
- This allows balance and height to be calculated in a single traversal.

Time Complexity: O(n)
Space Complexity: O(h)

where h is the height of the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def check(node):
            if node is None:
                return True, 0

            left_balanced, left_height = check(node.left)
            right_balanced, right_height = check(node.right)

            balanced = (
                left_balanced
                and right_balanced
                and abs(left_height - right_height) <= 1
            )

            height = 1 + max(left_height, right_height)

            return balanced, height

        balanced, _ = check(root)

        return balanced