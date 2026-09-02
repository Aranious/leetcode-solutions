from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = {}  # Number -> how many windows it appears in
        
        for left in range(n - k + 1):
            window = nums[left:left + k]
            # Get the distinct numbers in this window
            distinct = set(window)
            for num in distinct:
                count[num] = count.get(num, 0) + 1
        
        # Find the largest number that appears in exactly 1 window
        ans = -1
        for num, freq in count.items():
            if freq == 1:
                ans = max(ans, num)
        
        return ans