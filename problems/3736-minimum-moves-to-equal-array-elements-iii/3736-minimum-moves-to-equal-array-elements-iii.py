class Solution:
    def minMoves(self, nums: list[int]) -> int:
        maxx = max(nums)
        return sum(maxx - x for x in nums)