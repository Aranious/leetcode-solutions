# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node: Optional[TreeNode], is_left: bool) -> int:
            # Base case: empty node -> contributes nothing
            if not node:
                return 0
            
            # If this node is a leaf AND it is a left child:
            # We found a left leaf!
            if is_left and not node.left and not node.right:
                return node.val
            
            # Otherwise, keep searching. 
            # Pass 'True' when going left, 'False' when going right.
            return dfs(node.left, True) + dfs(node.right, False)
        
        return dfs(root, False)  # Root is not a left childe4