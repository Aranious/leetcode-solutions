class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        r1 = []
        r2 = []

        for i in range(len(nums)):
            r1.append(sum(nums[:i]))      # left sum
            r2.append(sum(nums[i+1:]))    # right sum

        final = []
        for a, b in zip(r1, r2):
            final.append(abs(a - b))

        return final