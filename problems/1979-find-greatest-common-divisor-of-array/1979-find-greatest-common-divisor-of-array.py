class Solution:
    def findGCD(self, nums: list[int]) -> int:
        minn, maxx = min(nums),max(nums)

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        return gcd(minn,maxx)