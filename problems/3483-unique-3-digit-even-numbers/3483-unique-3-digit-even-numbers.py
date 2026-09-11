from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        ans = set()
        
        for i in range(n):
            if digits[i] == 0:      # no leading zero
                continue
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue
                    if digits[k] % 2 == 0:   # last digit must be even
                        num = digits[i] * 100 + digits[j] * 10 + digits[k]
                        ans.add(num)
        
        return len(ans)