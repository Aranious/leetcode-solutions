class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        length_of_n = len(str(n))
        
        # Loop over each possible digit length (e.g., 1, 2, 3, ... up to length_of_n)
        for L in range(1, length_of_n + 1):
            # Start of the range for this length (e.g., for 4 digits, start = 1000)
            start = 10 ** (L - 1)
            # End of the range, but don't go past n (e.g., for 4 digits, end = 9999)
            end = min(n, 10 ** L - 1)
            
            # If the start is bigger than n, we are done
            if start > n:
                break
            
            # Count how many numbers have exactly this length
            count = end - start + 1
            
            # Comma per number for this length
            commas_per_number = (L - 1) // 3
            
            # Add all at once! (No loop!)
            total += count * commas_per_number
        
        return total