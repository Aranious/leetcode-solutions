# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(left: int, right: int) -> Optional[TreeNode]:
            # Base case: empty subarray
            if left > right:
                return None
            
            # Step 1: Find the middle
            mid = (left + right) // 2
            
            # Step 2: Create the root node
            root = TreeNode(nums[mid])
            
            # Step 3: Build left subtree from left half
            root.left = helper(left, mid - 1)
            
            # Step 4: Build right subtree from right half
            root.right = helper(mid + 1, right)
            
            return root
        
        return helper(0, len(nums) - 1)