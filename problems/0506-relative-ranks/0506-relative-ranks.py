class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        n = len(score)
        scored = [(s, i) for i, s in enumerate(score)]
        scored.sort(reverse=True)

        answer = [""] * n

        for place, (s, orig_idx) in enumerate(scored, start=1):
            if place == 1:
                answer[orig_idx] = "Gold Medal"
            elif place == 2:
                answer[orig_idx] = "Silver Medal"
            elif place == 3:
                answer[orig_idx] = "Bronze Medal"
            else:
                answer[orig_idx] = str(place)

        return answer