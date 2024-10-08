# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            l=dfs(node.left)
            r=dfs(node.right)
            ans=max(ans, l+r)
            return 1 + max(l, r)
        ans=0
        dfs(root)
        return ans
