class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        high = 0
        current = 0
        for i in gain:
            current += i
            if current > high:
                high = current
        return high