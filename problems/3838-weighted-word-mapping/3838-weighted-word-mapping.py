class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        return ''.join(
            chr(ord('z') - (sum(weights[ord(ch) - ord('a')] for ch in word) % 26))
            for word in words
        )