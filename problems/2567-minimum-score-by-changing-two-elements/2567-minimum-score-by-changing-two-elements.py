class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        return min(
            nums[n - 1] - nums[2],   # remove two smallest
            nums[n - 2] - nums[1],   # remove one smallest, one largest
            nums[n - 3] - nums[0],   # remove two largest
        )