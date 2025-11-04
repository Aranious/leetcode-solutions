from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        answer = []

        for i in range(n - k + 1):
            window = nums[i:i+k]
            
            # Count manually
            freq = {}
            for num in window:
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1

            # Sort by:
            # 1️⃣ frequency descending
            # 2️⃣ value descending (for tie-break)
            sorted_items = sorted(freq.items(), key=lambda item: (item[1], item[0]), reverse=True)

            # Pick top x and compute x-sum
            total_sum = 0
            for num, count in sorted_items[:x]:
                total_sum += num * count

            answer.append(total_sum)

        return answer