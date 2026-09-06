class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: If there's only 1 row, the zigzag is just a straight line.
        if numRows == 1:
            return s
        
        # Create a bucket for each row (list of strings)
        rows = [''] * numRows
        
        current_row = 0
        going_down = False  # We start at the top, so we need to go down first.
        
        for char in s:
            # Place the character in its row
            rows[current_row] += char
            
            # If we hit the very top (row 0) or very bottom (row numRows-1),
            # flip the direction.
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move to the next row (either down by 1, or up by 1)
            current_row += 1 if going_down else -1
        
        # Join all rows together
        return ''.join(rows)