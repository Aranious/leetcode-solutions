class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        words = set(word)
        result = 0
        for i in range(26):
            lower = chr(ord('a') + i)
            upper = chr(ord('A') + i)
            if lower in words and upper in words:
                result += 1
        return result