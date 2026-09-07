class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1]]

        for i in range(rowIndex):
            prev_row = triangle[-1]
            new_row = [1]

            for j in range(len(prev_row) - 1):
                new_row.append(prev_row[j] + prev_row[j + 1])
            
            new_row.append(1)         # End the new row with a 1
            triangle.append(new_row)  # Save it

        return triangle[-1]