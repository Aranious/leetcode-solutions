class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = 0
        while n >= k + 1:   # While we have enough for the next row
            k += 1          # Build the row
            n -= k          # Spend the coins for that row
        return k