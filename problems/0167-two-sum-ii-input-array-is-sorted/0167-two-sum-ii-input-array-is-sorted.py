class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s_map = {}
        for idx, num in enumerate(numbers):   # idx = index, num = value
            complement = target - num
            if complement in s_map:
                return [s_map[complement] + 1, idx + 1]  # 1-based indices
            s_map[num] = idx