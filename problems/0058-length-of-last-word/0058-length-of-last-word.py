class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list = s.split()
        print(word_list)
        return len(word_list[-1])