class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        # map each letter to its Morse code
        memo = {}
        for i in range(26):
            memo[chr(ord('a') + i)] = morse[i]
        
        # build the Morse string for each word
        transformations = set()
        for word in words:
            morse_word = ""
            for ch in word:
                morse_word += memo[ch]
            transformations.add(morse_word)
        
        return len(transformations)