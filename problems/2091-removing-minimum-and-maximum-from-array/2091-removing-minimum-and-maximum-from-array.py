class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minn = min(nums)
        maxx = max(nums)

        min_counter = 0
        max_counter = 0

        result1 = []

        # Remove minimum from the front
        for i in range(len(nums)):
            min_counter += 1
            if nums[i] == minn:
                break

        result1.append(min_counter)

        min_counter = 0
        max_counter = 0

        # Remove minimum from the back
        for i in range(len(nums) - 1, -1, -1):
            min_counter += 1
            if nums[i] == minn:
                break

        result1.append(min_counter)

        # Remove maximum from the front
        for i in range(len(nums)):
            max_counter += 1
            if nums[i] == maxx:
                break

        result1.append(max_counter)

        max_counter = 0

        # Remove maximum from the back
        for i in range(len(nums) - 1, -1, -1):
            max_counter += 1
            if nums[i] == maxx:
                break

        result1.append(max_counter)

        return min(
            max(result1[0], result1[2]),
            max(result1[1], result1[3]),
            result1[0] + result1[3],
            result1[2] + result1[1]
        )