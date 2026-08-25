class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Count frequencies of each character
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        length = 0
        has_odd = False
        
        # Sum up all the even pairs
        for count in freq.values():
            length += count // 2 * 2
            if count % 2 == 1:
                has_odd = True
        
        # Add one odd character to the center if possible
        if has_odd:
            length += 1
        
        return length