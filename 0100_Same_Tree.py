"""
Problem: Same Tree
LeetCode: 100
Difficulty: Easy

Topic:
- Binary Tree
- Depth-First Search
- Recursion

Approach:
- Compare the two trees recursively.
- If both nodes are None, they are identical at that position.
- If only one node is None, the structures are different.
- If their values differ, the trees are different.
- Recursively compare the left and right subtrees.

Time Complexity: O(n)
Space Complexity: O(h)

where:
- n = number of nodes compared
- h = height of the tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(
        self,
        p: Optional[TreeNode],
        q: Optional[TreeNode]
    ) -> bool:

        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        left_tree = self.isSameTree(p.left, q.left)
        right_tree = self.isSameTree(p.right, q.right)

        return left_tree and right_tree