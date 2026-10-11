class Solution:
    def threeFibonacciSum(self, n: int) -> bool:


        a, b = 0, 1

        while True:
            c = a + b
            s = a + b + c

            if s == n:
                return True
            if s > n:
                return False

            a, b = b, c