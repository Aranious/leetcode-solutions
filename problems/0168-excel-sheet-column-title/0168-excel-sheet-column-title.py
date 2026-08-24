class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        
        while columnNumber > 0:
            # Step 1: Shift to 0-indexed (the "Excel twist")
            columnNumber -= 1
            
            # Step 2: Get the remainder (0-25) -> maps to A-Z
            remainder = columnNumber % 26
            
            # Step 3: Convert to character (A=65 in ASCII)
            result.append(chr(ord('A') + remainder))
            
            # Step 4: Move to the next digit
            columnNumber //= 26
        
        # The digits are built in reverse order
        return ''.join(reversed(result))