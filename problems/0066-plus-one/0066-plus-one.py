class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string1 = "".join(map(str, digits)) 

        sum = str(int(string1) + 1)

        result = list(map(int,sum))
        return result