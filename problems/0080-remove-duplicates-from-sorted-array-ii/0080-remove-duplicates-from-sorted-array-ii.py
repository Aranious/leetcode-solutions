from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        # k+=1 
        
        seen = {}
        
        for i in range(len(nums)):
            val = nums[i]
            seen[val] = seen.get(val, 0) + 1
            if seen[val] <= 2:
                nums[k] = val
                k += 1

# print(nums[:k])  # [1, 2, 2, 3, 3, 4]


        return k