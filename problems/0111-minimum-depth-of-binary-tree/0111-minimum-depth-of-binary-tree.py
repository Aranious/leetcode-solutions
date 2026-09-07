# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # Base case: empty node
            if not node:
                return 0
            
            # If there is no left child, we MUST go right
            if not node.left:
                return 1 + dfs(node.right)
            
            # If there is no right child, we MUST go left
            if not node.right:
                return 1 + dfs(node.left)
            
            # If both children exist, take the smaller one
            return 1 + min(dfs(node.left), dfs(node.right))
        
        return dfs(root)