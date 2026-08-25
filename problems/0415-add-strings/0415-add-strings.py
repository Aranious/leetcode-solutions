class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1  # Pointer for num1 (rightmost)
        j = len(num2) - 1  # Pointer for num2 (rightmost)
        carry = 0
        result = []
        
        # LOOK FAMILIAR? while l1 or l2 or carry:
        while i >= 0 or j >= 0 or carry:
            # Convert a SINGLE character to a number (NOT the whole string)
            # ord('3') - ord('0') = 51 - 48 = 3
            digit1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            digit2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            
            total = digit1 + digit2 + carry
            # write this
            digit = total % 10
            # carry this
            carry = total // 10
            
            
            # Append the digit as a character
            result.append(chr(digit + ord('0')))
            
            # Move the pointers left
            i -= 1
            j -= 1
        
        # We built it backwards (units place first), so reverse it!
        return ''.join(result[::-1])