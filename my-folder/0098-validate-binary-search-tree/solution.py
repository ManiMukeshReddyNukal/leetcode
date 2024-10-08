# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack=[(root,-math.inf,math.inf)]
        while stack:
            node,lower,higher=stack.pop()
            if not node:
                continue
            val=node.val
            if val<=lower or val>=higher:
                return False
            stack.append((node.right,val,higher))
            stack.append((node.left,lower,val))
        return True
