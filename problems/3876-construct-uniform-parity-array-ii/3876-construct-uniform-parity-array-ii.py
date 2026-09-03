from typing import List

class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        odds = [x for x in nums1 if x % 2 == 1]
        evens = [x for x in nums1 if x % 2 == 0]
        
        # If one of the groups is empty, we just keep all numbers (uniform parity)
        if not odds or not evens:
            return True
        
        # Otherwise, we MUST target "all odd".
        # Check if the smallest odd is smaller than the smallest even.
        return min(odds) < min(evens)