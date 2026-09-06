class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Step 1: Pre‑compute prefix max (from left to right)
        prefix_max = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], nums[i])
        
        # Step 2: Pre‑compute suffix min (from right to left)
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suffix_min[i] = min(suffix_min[i+1], nums[i])
        
        # Step 3: Check each index in O(1) time
        for i in range(n):
            if prefix_max[i] - suffix_min[i] <= k:
                return i
        
        return -1