class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matchh = bool
        for i in matrix :
            if matchh == True:
                return True 
            if target in i:
                return True
            elif target not in i:
                matchh = False
        return matchh