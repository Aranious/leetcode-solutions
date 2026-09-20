from typing import List

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:
        
        min_land_finish = min(
            s + d for s, d in zip(landStartTime, landDuration)
        )
        min_water_finish = min(
            s + d for s, d in zip(waterStartTime, waterDuration)
        )
        
        # Land first, then water
        land_then_water = min(
            max(min_land_finish, ws) + wd
            for ws, wd in zip(waterStartTime, waterDuration)
        )
        
        # Water first, then land
        water_then_land = min(
            max(min_water_finish, ls) + ld
            for ls, ld in zip(landStartTime, landDuration)
        )
        
        return min(land_then_water, water_then_land)