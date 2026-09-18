class Solution:
    def maxProduct(self, n: int) -> int:
        lisst = []
        digits = list(str(n))

        biggest = max(digits)
        lisst.append(int(biggest))

        digits.remove(biggest)

        second = max(digits)
        lisst.append(int(second))

        return lisst[0] * lisst[1]