class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        kk = k

        if kk not in nums:
            return kk
        
        max_k = 0
        min_k = 0
        for num in nums:
            if num % kk == 0:
                max_k = max(max_k,num)
        

        while min_k <= max_k:
            
            min_k += k
            if min_k not in nums:
                return min_k
        return max_k + k