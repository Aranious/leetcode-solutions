class Solution:
    def dominantIndex(self, nums: list[int]) -> int:

        # Pass 1: Find the max value and its index
        max_val = max(nums)
        max_idx = nums.index(max_val)
        
        # Pass 2: Check if max_val is at least twice every other number
        for i, x in enumerate(nums):
            if i != max_idx and max_val < 2 * x:
                return -1
                
        return max_idx