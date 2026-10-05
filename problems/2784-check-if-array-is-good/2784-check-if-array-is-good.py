from collections import Counter

class Solution:
    def isGood(self, nums: list[int]) -> bool:
        n = len(nums) - 1
        
        if n < 1:
            return False
        
        count = Counter(nums)
        
        # n must appear exactly twice
        if count[n] != 2:
            return False
        
        # 1 through n-1 must appear exactly once
        for i in range(1, n):
            if count[i] != 1:
                return False
        
        # no other numbers allowed
        for key in count:
            if key < 1 or key > n:
                return False
        
        return True