class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0  # pointer for position of non-val elements
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # move element to the "front"
                k += 1
        return k