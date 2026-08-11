"""
Problem: Path Sum
LeetCode: 112
Difficulty: Easy

Topic:
- Binary Tree
- Depth-First Search
- Recursion

Approach:
- Subtract the current node's value from the remaining target sum.
- When a leaf node is reached, check whether the remaining sum is 0.
- Recursively check the left and right subtrees.
- Return True if either subtree contains a valid root-to-leaf path.

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
    def hasPathSum(
        self,
        root: Optional[TreeNode],
        targetSum: int
    ) -> bool:

        if root is None:
            return False

        remaining = targetSum - root.val

        if root.left is None and root.right is None:
            return remaining == 0

        return (
            self.hasPathSum(root.left, remaining)
            or self.hasPathSum(root.right, remaining)
        )