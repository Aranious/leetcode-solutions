# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Rule 1: Both are None -> True
        if not p and not q:
            return True
        
        # Rule 2: One is None, the other isn't -> False
        # (This also catches if both are None? No, but we already checked that above)
        if not p or not q:
            return False
        
        # Rule 3: Values don't match -> False
        if p.val != q.val:
            return False
        
        # Rule 4: Values match! Now check the entire left side AND entire right side.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)