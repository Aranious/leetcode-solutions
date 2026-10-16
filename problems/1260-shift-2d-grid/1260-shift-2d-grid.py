class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m = len(grid)
        n = len(grid[0])
        total = m * n
        k = k % total

        # flatten
        flat = []
        for row in grid:
            for val in row:
                flat.append(val)

        # rotate right by k
        rotated = flat[-k:] + flat[:-k]

        # reshape back into m rows of n
        result = []
        for i in range(m):
            result.append(rotated[i * n : (i + 1) * n])

        return result