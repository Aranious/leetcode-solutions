from typing import List
from math import gcd

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        best = 0

        for i in range(n):
            prod = 1
            g = 0
            l = 1

            for j in range(i, n):
                x = nums[j]

                prod *= x
                g = gcd(g, x)
                l = l // gcd(l, x) * x

                if prod == g * l:
                    best = max(best, j - i + 1)

        return best