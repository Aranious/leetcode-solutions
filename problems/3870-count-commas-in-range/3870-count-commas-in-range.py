class Solution:
    def countCommas(self, n: int) -> int:
        commas = 0
        for i in range(1000,n+1):
            L = len(str(i))
            commas += (L - 1) // 3
        return commas