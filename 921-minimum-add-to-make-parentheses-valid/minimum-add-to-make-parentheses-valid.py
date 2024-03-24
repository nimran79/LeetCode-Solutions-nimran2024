class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s:
            return 0
        
        # Variables to count the necessary additions and keeping track of the unmatched parentheses.
        unmatched_open = additions_needed = 0

        for i in range(len(s)):
            # If the character is an open parenthesis, increment the unmatched count.
            if s[i] == '(':
                unmatched_open += 1
            # If it's a close parenthesis and there's an unmatched open, pair it and decrement.
            elif unmatched_open:
                unmatched_open -= 1
            # Otherwise, if there is no unmatched open, we need an addition (an open parenthesis).
            else:
                additions_needed += 1
        
        # Add any remaining unmatched open parentheses to the total additions needed.
        additions_needed += unmatched_open
      
        # Return the total number of additions needed to make the string valid.
        return additions_needed
