from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:  # If array has 0 or 1 element, no jumps needed
            return 0
        
        jumps = 0  # Count of jumps
        current_end = 0  # End of the current jump's reachable range
        farthest = 0  # Farthest index reachable with the next jump
        
        for i in range(len(nums) - 1):  # Stop before the last index
            farthest = max(farthest, i + nums[i])  # Update farthest reachable index
            
            if i == current_end:  # Reached the end of current jump's range
                jumps += 1  # Take a new jump
                current_end = farthest  # New range extends to farthest
                if current_end >= len(nums) - 1:  # If we can reach the last index
                    break
        
        return jumps