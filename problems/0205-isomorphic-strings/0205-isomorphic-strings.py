class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            # If we've seen c1 before, check it maps consistently
            if c1 in s_map:
                if s_map[c1] != c2:
                    return False
            else:
                s_map[c1] = c2

            # Also check the reverse mapping (to prevent two different chars mapping to same char)
            if c2 in t_map:
                if t_map[c2] != c1:
                    return False
            else:
                t_map[c2] = c1

        return True