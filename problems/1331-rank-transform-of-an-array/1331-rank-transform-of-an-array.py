class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        arr2 = sorted(set(arr))
        dic = {}

        for i in range(1,len(arr2)+1):
            
            dic[arr2[i-1]] = i
        result = []
        for i in range(len(arr)):
            result.append(dic[arr[i]])
        return result