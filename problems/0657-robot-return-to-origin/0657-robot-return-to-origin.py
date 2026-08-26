class Solution:
    def judgeCircle(self, moves: str) -> bool:
        from collections import Counter

        counts = Counter(moves)

        return counts["U"] == counts["D"] and counts["R"] == counts["L"]