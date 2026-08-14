"""
Problem: Binary Tree Postorder Traversal
LeetCode: 145
Difficulty: Easy

Topic:
- Binary Tree
- Depth-First Search
- Recursion
- Postorder Traversal

Approach:
- Recursively traverse the left subtree.
- Recursively traverse the right subtree.
- Visit the current node after both subtrees.
- Return the values in Left -> Right -> Root order.

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
    def postorderTraversal(
        self,
        root: Optional[TreeNode]
    ) -> List[int]:

        if root is None:
            return []

        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)

        return left + right + [root.val]