class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort()
        n = len(cost)
        total = 0
        i = 1

        while i <= n:
            # buy the largest remaining candy
            total += cost[-i]

            # buy the second largest remaining candy, if it exists
            if i + 1 <= n:
                total += cost[-(i + 1)]

            # skip the third one because it's free
            i += 3

        return total