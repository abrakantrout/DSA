"""
Problem: Binary Tree Inorder Traversal
LeetCode: 94
Difficulty: Easy

Topic:
- Binary Tree
- Depth-First Search
- Recursion
- Inorder Traversal

Approach:
- Visit the left subtree first.
- Process the current node.
- Visit the right subtree.
- Store each visited node's value in the result list.

Time Complexity: O(n)
Space Complexity: O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)

        return result