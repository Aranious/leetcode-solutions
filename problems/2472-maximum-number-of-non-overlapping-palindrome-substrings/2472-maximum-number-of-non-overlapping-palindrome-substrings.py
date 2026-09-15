class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        def is_pal(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        for i in range(1, n + 1):
            # Option 1: skip s[i-1]
            dp[i] = dp[i - 1]

            # Option 2: take palindrome of length k ending at i-1
            if i >= k and is_pal(i - k, i - 1):
                dp[i] = max(dp[i], dp[i - k] + 1)

            # Option 3: take palindrome of length k+1 ending at i-1
            if i >= k + 1 and is_pal(i - k - 1, i - 1):
                dp[i] = max(dp[i], dp[i - k - 1] + 1)

        return dp[n]