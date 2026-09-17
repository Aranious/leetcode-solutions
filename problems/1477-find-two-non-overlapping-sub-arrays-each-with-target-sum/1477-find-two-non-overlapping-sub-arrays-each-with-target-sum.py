from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')
        
        # left[i] = min length of subarray with sum target ending at or before i
        left = [INF] * n
        prefix = 0
        seen = {0: -1}          # prefix sum -> latest index
        best = INF
        
        for i in range(n):
            prefix += arr[i]
            if prefix - target in seen:
                length = i - seen[prefix - target]
                best = min(best, length)
            left[i] = best
            seen[prefix] = i    # store latest index for this prefix sum
        
        # right[i] = min length of subarray with sum target starting at or after i
        right = [INF] * n
        suffix = 0
        seen = {0: n}           # suffix sum -> earliest index (from right)
        best = INF
        
        for i in range(n - 1, -1, -1):
            suffix += arr[i]
            if suffix - target in seen:
                length = seen[suffix - target] - i
                best = min(best, length)
            right[i] = best
            seen[suffix] = i    # store smallest index for this suffix sum
        
        # Try every split point between i and i+1
        ans = INF
        for i in range(n - 1):
            if left[i] != INF and right[i + 1] != INF:
                ans = min(ans, left[i] + right[i + 1])
        
        return -1 if ans == INF else ans