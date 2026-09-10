# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(node):
            nonlocal ans
            
            # Base case: empty node has sum 0 and count 0
            if not node:
                return (0, 0)   # (sum, count)
            
            # Get left subtree info
            left_sum, left_count = dfs(node.left)
            
            # Get right subtree info
            right_sum, right_count = dfs(node.right)
            
            # Combine everything
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            
            # Calculate average (rounded down)
            average = total_sum // total_count
            
            # If this node equals the average, count it
            if node.val == average:
                ans += 1
            
            # Return this subtree's sum and count to the parent
            return (total_sum, total_count)
        
        dfs(root)
        return ans