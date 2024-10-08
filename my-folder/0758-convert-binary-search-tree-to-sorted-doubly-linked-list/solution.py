"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        first,last=None,None
        def process(node):
            nonlocal first,last
            if node:
                process(node.left)
                if last:
                    last.right=node
                    node.left=last
                else:
                    first=node
                last=node
                process(node.right)
            if not node:
                return None
        process(root)
        last.right=first
        first.left=last
        return first    
