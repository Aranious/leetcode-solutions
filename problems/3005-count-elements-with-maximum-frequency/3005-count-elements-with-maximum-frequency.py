class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        current_max = 0
        nums_map = {}
        for i in nums:
            nums_map[i] = nums_map.get(i, 0) +1
        for i in nums_map:
            if nums_map[i]>= current_max:
                current_max = nums_map[i]
        new_list = []
        for i in nums_map:
            if nums_map[i] == current_max:
                print(i)
                new_list.append(nums_map[i])
        return sum(new_list)