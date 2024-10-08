# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            l,r=dfs(node.left),dfs(node.right)
            ans+=abs(l)+abs(r)
            return l+r+node.val-1
        dfs(root)
        return ans
