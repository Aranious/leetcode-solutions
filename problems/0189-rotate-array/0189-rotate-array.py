class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums.reverse()                 # reverse entire list
        nums[:k] = reversed(nums[:k]) # reverse first k elements
        nums[k:] = reversed(nums[k:]) # reverse remaining elements