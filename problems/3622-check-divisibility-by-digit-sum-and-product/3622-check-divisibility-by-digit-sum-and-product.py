class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = [int(c) for c in str(n)]
        digit_sum = sum(digits)
        digit_product = 1
        for d in digits:
            digit_product *= d
        total = digit_sum + digit_product
        return n % total == 0