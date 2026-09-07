# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            # Base case: Empty tree has height 0
            if not node:
                return 0
            
            # 1. Get the height of the left subtree
            left_height = dfs(node.left)
            # If left subtree is unbalanced, propagate -1 up immediately
            if left_height == -1:
                return -1
            
            # 2. Get the height of the right subtree
            right_height = dfs(node.right)
            # If right subtree is unbalanced, propagate -1 up immediately
            if right_height == -1:
                return -1
            
            # 3. Check the current node
            if abs(left_height - right_height) > 1:
                return -1  # Unbalanced! Send a signal up.
            
            # 4. Return the actual height of this node
            return 1 + max(left_height, right_height)
        
        # If dfs returns -1, it's false. Otherwise, it's true.
        return dfs(root) != -1