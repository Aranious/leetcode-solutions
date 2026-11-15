class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        best = float('inf')
        n = len(nums)
        for i in range(n):              # start index
            for k in range(l, r + 1):   # length
                if i + k > n:           # subarray goes past the end
                    break
                s = sum(nums[i : i + k])
                if s > 0:
                    best = min(best, s)

        return best if best != float('inf') else -1