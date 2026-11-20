class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            groups = [sum(map(int, s[i:i+k])) for i in range(0, len(s), k)]
            s = "".join(map(str, groups))
        return s