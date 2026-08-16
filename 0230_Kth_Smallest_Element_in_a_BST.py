"""
Problem: Kth Smallest Element in a BST
LeetCode: 230
Difficulty: Medium

Topic:
- Binary Search Tree
- Depth-First Search
- Inorder Traversal
- Stack

Approach:
- Perform an iterative inorder traversal using a stack.
- In a BST, inorder traversal visits nodes in ascending order.
- Decrement k each time a node is visited.
- When k reaches 0, the current node is the kth smallest element.

Time Complexity: O(h + k)
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            k -= 1

            if k == 0:
                return root.val

            root = root.right