# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # A helper function to check if two trees are mirrors of each other
        def isMirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            # Rule 1: Both are empty -> Perfect mirror
            if not t1 and not t2:
                return True
            
            # Rule 2: One is empty, the other isn't -> Not a mirror
            if not t1 or not t2:
                return False
            
            # Rule 3: Values must match
            if t1.val != t2.val:
                return False
            
            # Rule 4: Values match!
            # The LEFT of t1 must mirror the RIGHT of t2
            # AND the RIGHT of t1 must mirror the LEFT of t2
            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        
        # An empty tree is symmetric
        if not root:
            return True
        
        # Start the mirror check: left subtree vs right subtree
        return isMirror(root.left, root.right)