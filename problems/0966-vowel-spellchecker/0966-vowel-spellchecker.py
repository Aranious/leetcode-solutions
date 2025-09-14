from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set("aeiou")

        # Step 1: Exact match set
        exact_words = set(wordlist)

        # Step 2: Case-insensitive mapping: lowercase -> first occurrence in wordlist
        case_map = {}
        for word in wordlist:
            key = word.lower()
            if key not in case_map:
                case_map[key] = word

        # Step 3: Vowel-error mapping: lowercase with vowels replaced by '*'
        def devowel(word):
            return ''.join('*' if c in vowels else c for c in word.lower())

        vowel_map = {}
        for word in wordlist:
            key = devowel(word)
            if key not in vowel_map:
                vowel_map[key] = word

        # Step 4: Process queries
        result = []
        for query in queries:
            if query in exact_words:
                # Exact match (case-sensitive)
                result.append(query)
            elif query.lower() in case_map:
                # Case-insensitive match
                result.append(case_map[query.lower()])
            elif devowel(query) in vowel_map:
                # Vowel-error match
                result.append(vowel_map[devowel(query)])
            else:
                # No match
                result.append("")

        return result