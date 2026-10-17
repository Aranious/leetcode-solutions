class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def digit_sum(x: int) -> int:
            return sum(int(ch) for ch in str(x))

        n = len(nums)

        target = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {value: i for i, value in enumerate(target)}

        visited = [False] * n
        cycles = 0

        for i in range(n):
            if not visited[i]:
                cycles += 1
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = pos[nums[j]]

        return n - cycles