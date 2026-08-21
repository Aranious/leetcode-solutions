# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, List

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def dfs(node):
            if not node:
                return
            
            # 1. Go Left
            dfs(node.left)
            
            # 2. Visit Root (append value)
            result.append(node.val)
            
            # 3. Go Right
            dfs(node.right)
        
        dfs(root)
        return result