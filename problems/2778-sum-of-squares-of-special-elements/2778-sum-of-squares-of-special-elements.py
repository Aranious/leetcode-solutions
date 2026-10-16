class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(1, n + 1):      # 1-indexed positions
            if n % i == 0:             # position divides n
                total += nums[i - 1] ** 2   # value at that position, squared
        return total