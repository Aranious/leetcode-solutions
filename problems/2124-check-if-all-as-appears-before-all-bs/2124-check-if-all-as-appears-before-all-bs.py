class Solution:
    def checkString(self, s: str) -> bool:
        seen_b = False
        for ch in s:
            if ch == 'b':
                seen_b = True
            elif seen_b:   # so we would just trigger the b as long as there is b in the mix. if we encounter the a after there was a b seen. then it is not right. 
                return False
        return True