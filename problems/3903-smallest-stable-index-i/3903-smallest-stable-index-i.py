class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        for i in range(n):
            # max from 0 to i (inclusive)
            curMax = max(nums[:i+1])
            # min from i to end (inclusive)
            curMin = min(nums[i:])
            
            if curMax - curMin <= k:
                return i
        
        return -1