class Solution:
    def reverse(self, x: int) -> int:
        nlist = []
        for i in str(x):
            nlist.append(i)
        nlist.reverse()
        
        if "-" in nlist:
            nlist.remove("-")
            result = int("-" + "".join(nlist))
        else:
            result = int("".join(nlist))
        
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result