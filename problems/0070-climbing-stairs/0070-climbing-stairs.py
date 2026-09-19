class Solution:
    def climbStairs(self, n: int) -> int:
        # dp(0) = 1
        # dp(1) = 1

        # # first base cases
        # # second the transition state
        # dp(n) = dp(n-1)= dp(n-2)
        # here is what i think i gotta do.
        # firstly i define a dp func
        # i give it the base cases and force it to start the recursion
        # then i call it in the outer function with the n. 
        memo = {}
        def dp(i):
            # if i am not wrong only one way to not take any steps right?
            if i<=1:
                return 1
            if i in memo:
                return memo[i]
            memo[i] = dp(i - 1) + dp(i - 2)   # <-- this line was missing
            return memo[i]
        return dp(n)