class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1
        
        inc = 1
        dec = 1
        best = 1
        counter = 0
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc += 1
                dec = 1          # decreasing run is broken
            elif nums[i] < nums[i-1]:
                dec += 1
                inc = 1          # increasing run is broken
            else:
                inc = 1
                dec = 1          # equal breaks both runs
            
            best = max(best, inc, dec)
        
        return best