from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]
        i = 1
        
        # Extend the sequential prefix as long as possible
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1
        
        # Find the smallest missing integer >= total
        seen = set(nums)
        while total in seen:
            total += 1
        
        return total