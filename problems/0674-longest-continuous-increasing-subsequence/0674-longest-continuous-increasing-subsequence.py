class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        n = len(nums)
        best = 1

        for i in range(n):
            counter = 1
            while True:
                if i + counter >= n:
                    break
                if nums[i + counter - 1] < nums[i + counter]:
                    counter += 1
                    best = max(best, counter)
                else:
                    break

        return best