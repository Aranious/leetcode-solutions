class Solution:
    def getStrongest(self, arr: list[int], k: int) -> list[int]:
        arr.sort()
        n = len(arr)
        m = arr[(n - 1) // 2]        # median
        arr.sort(key=lambda x: (abs(x - m), x), reverse=True)
        return arr[:k]

        # arr.sort(key=lambda x: abs(m-x),x)