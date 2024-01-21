# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ######   print root, self left , self  right 
        if not root:
            return None
        if not root.left and not root.right:
            return root
        lefttail=self.flatten(root.left)
        righttail=self.flatten(root.right)
        if lefttail:
            lefttail.right=root.right
            root.right=root.left
            root.left=None
        return righttail if righttail else lefttail

