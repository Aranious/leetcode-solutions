class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current = []  # This is like your 'result' list in Inorder traversal!

        def backtrack(start_index, remaining):
            # Base Case 1: We found a valid combination
            if remaining == 0:
                result.append(current[:])  # COPY the current path (Important!)
                return
            
            # Base Case 2: Dead end (overshot target)
            if remaining < 0:
                return
            
            # Recursive Case: Try each candidate from 'start_index' onwards
            # Why start_index? To avoid duplicates like [2,3] and [3,2]
            for i in range(start_index, len(candidates)):
                # Choose the candidate
                current.append(candidates[i])
                
                # Recurse with the SAME i (because we can reuse the same number!)
                backtrack(i, remaining - candidates[i])
                
                # Backtrack! Undo the choice (This is the 'pop' that cleans up)
                current.pop()
        
        backtrack(0, target)
        return result