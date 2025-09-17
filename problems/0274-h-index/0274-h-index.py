class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        citations.sort(reverse=True)
        for i, c in enumerate(citations, start=1):  # i is paper count (1-based)
            if c >= i:
                h = i
            else:
                break
        return h # 3