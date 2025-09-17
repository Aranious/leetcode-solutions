class Solution:
    def romanToInt(self, s: str) -> int:
        # Initialize value map and index map
        value_map = {}
        symbols_indexes = {}
        values = [1, 5, 10, 50, 100, 500, 1000]
        symbols = "IVXLCDM"
        for i, symbol in enumerate(symbols):
            value_map[symbol] = values[i]
            symbols_indexes[symbol] = i
        
        result = 0
        i = 0
        
        while i < len(s):
            # If current numeral is followed by a higher-order numeral, subtract
            if i + 1 < len(s) and symbols_indexes[s[i]] < symbols_indexes[s[i + 1]]:
                result += value_map[s[i + 1]] - value_map[s[i]]
                i += 2
            else:
                result += value_map[s[i]]
                i += 1
        
        return result