class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        even = 1   # prefix[0] = 0 is even
        odd = 0
        running = 0
        ans = 0

        for x in arr:
            running += x
            if running % 2 == 1:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1

        return ans % MOD