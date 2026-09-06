class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        counts = {}

        for char in s:
            counts[char] = counts.get(char, 0) + 1
        
        # NEW: Count how many of each character we need in target
        target_counts = {}
        for char in target:
            target_counts[char] = target_counts.get(char, 0) + 1
        
        hm = []
        # CHANGED: Loop over the unique characters in target_counts (not the whole target)
        for char, needed in target_counts.items():
            if char not in counts:
                return 0
            # CHANGED: Divide the available count by how many we need per copy
            hm.append(counts[char] // needed)
        
        return min(hm)