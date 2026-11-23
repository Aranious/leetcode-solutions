class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        # Step 1: map each sum of nums1[i] + nums2[j] to its count
        pair_sum_count = defaultdict(int)
        for a in nums1:
            for b in nums2:
                pair_sum_count[a + b] += 1

        # Step 2: for each nums3[k] + nums4[l], add count of -(sum)
        count = 0
        for c in nums3:
            for d in nums4:
                count += pair_sum_count[-(c + d)]

        return count