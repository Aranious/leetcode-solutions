class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        seen = {}
        for i in range(len(nums)):
            the_key = nums[i]
            seen[the_key] = seen.get(the_key,  0) + 1
        max_key = max(seen, key=seen.get)
        return max_key