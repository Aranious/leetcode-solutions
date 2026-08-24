class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        start = 0
        max_length = 1
        
        def expand_around_center(left: int, right: int) -> tuple:
            # Expand while we're within bounds and characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the start index and length of the palindrome
            # (left+1 because we overshot by 1, right-left-1 because we overshot)
            return left + 1, right - left - 1
        
        for center in range(len(s)):
            # Check odd-length palindromes (center is a character)
            left, length = expand_around_center(center, center)
            if length > max_length:
                max_length = length
                start = left
            
            # Check even-length palindromes (center is between two characters)
            left, length = expand_around_center(center, center + 1)
            if length > max_length:
                max_length = length
                start = left
        
        return s[start:start + max_length]