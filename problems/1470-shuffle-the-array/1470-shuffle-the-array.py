class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        mid = 0 + (len(nums) - 1 - 0) // 2
        l1 = nums[:mid + 1]
        l2 = nums[mid + 1:]

        result = []
        for i in range(len(l1)):
            result.append(l1[i])
            result.append(l2[i])
        return result