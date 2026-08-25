class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Step 1: Get distinct numbers
        distinct_nums = list(set(nums))
        
        # Step 2: Sort in descending order
        distinct_nums.sort(reverse=True)
        
        # Step 3: If there are at least 3 distinct numbers, return the 3rd one (index 2)
        if len(distinct_nums) >= 3:
            return distinct_nums[2]
        else:
            # Otherwise, return the maximum (first element)
            return distinct_nums[0]