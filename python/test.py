# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        return

    def getHeightNodes(self, root, h):
        ret = list()
        height = 1
        if h == 1:
            return root
        
        q = deque()

        while root:
            left = root.left
            right = root.right
            
        
