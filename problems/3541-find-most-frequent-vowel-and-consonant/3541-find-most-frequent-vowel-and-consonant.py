from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set("aeiou")
        consonants = set("abcdefghijklmnopqrstuvwxyz") - vowels

        # Separate vowels and consonants
        vowel_list = [ch for ch in s if ch in vowels]
        consonant_list = [ch for ch in s if ch in consonants]

        # Count frequencies
        counts_vowels = Counter(vowel_list)
        counts_consonants = Counter(consonant_list)

        # Get most frequent vowel/consonant safely
        max_vowel_letter = max(counts_vowels, key=counts_vowels.get, default="")
        max_consonant_letter = max(counts_consonants, key=counts_consonants.get, default="")

        max_vowel_count = counts_vowels.get(max_vowel_letter, 0)
        max_consonant_count = counts_consonants.get(max_consonant_letter, 0)

        
        return max_consonant_count + max_vowel_count