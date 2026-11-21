class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cs, ct = {}, {}
        for a, b in zip(s, t):
            cs[a] = cs.get(a, 0) + 1
            ct[b] = ct.get(b, 0) + 1

        return cs == ct