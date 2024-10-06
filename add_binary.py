class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []  # This will store the result in reverse order
        carry = 0
        
        i, j = len(a) - 1, len(b) - 1  # Pointers for the two strings
        
        # Loop while there are digits left in either string or there's a carry
        while i >= 0 or j >= 0 or carry:
            # Get the current digits (if out of bounds, use 0)
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            
            # Sum the digits and the carry
            total = digit_a + digit_b + carry
            
            # Update the result (total % 2 gives the binary digit to add)
            result.append(str(total % 2))
            
            # Update carry (total // 2 gives the new carry)
            carry = total // 2
            
            # Move the pointers
            i -= 1
            j -= 1
        
        # The result is currently reversed, so reverse it back
        return ''.join(result[::-1])
