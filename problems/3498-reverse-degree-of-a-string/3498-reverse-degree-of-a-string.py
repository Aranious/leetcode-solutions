class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for idx, ch in enumerate(s, start=1):
            value = 123 - ord(ch)
            total += idx * value
        return total