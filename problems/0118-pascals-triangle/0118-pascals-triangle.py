class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Start with the first row
        triangle = [[1]]
        
        # Build each row after the first
        for i in range(1, numRows):  # i goes from 1 to numRows-1
            prev_row = triangle[-1]   # Get the last row we just made
            new_row = [1]             # Start the new row with a 1
            
            # Add adjacent pairs from the previous row
            for j in range(len(prev_row) - 1):
                new_row.append(prev_row[j] + prev_row[j + 1])
            
            new_row.append(1)         # End the new row with a 1
            triangle.append(new_row)  # Save it
            
        return triangle