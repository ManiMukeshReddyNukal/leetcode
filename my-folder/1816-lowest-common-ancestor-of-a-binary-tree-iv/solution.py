# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        if not root:
            return None
        if root in nodes:
            return root
        left=self.lowestCommonAncestor(root.left, nodes)
        right=self.lowestCommonAncestor(root.right, nodes)
        if left is not None and right is not None:
            return root
        else:
            return left or right
