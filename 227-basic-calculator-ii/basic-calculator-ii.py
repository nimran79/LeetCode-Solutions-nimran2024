class Solution:
    def calculate(self, s: str) -> int:
        prev = cur = res = 0
        cur_operation = "+"
        i = 0

        # Iterate over each character in the input string
        while i < len(s):
            cur_char = s[i] # store the current character

            # Check if the current char is a digit
            if cur_char.isdigit():
                # update 'cur' to be the current multi-digit number
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i += 1

                # Need to decrement i since it will contain a operation(+-*/) now
                i -= 1

                # Perform an action depending on the current operation 
                # For "+" or "-", we do not need to worry about operation priority
                if cur_operation == "+":
                    res += cur
                    prev = cur
                elif cur_operation == "-":
                    res -= cur
                    prev = -cur
                elif cur_operation == "*":
                    # Need to substract the previous number before performing * or /
                    res -= prev
                    res += prev * cur
                    prev = prev * cur
                else:
                    res -= prev
                    # Use division to round towards zero (// will not handle negative numbers correctly)
                    res += int(prev / cur)  
                    prev = int(prev / cur)
                
                cur = 0 # Reset 'cur' for the next number.
            elif cur_char != " ":
                # assign current char as operation that will be used in next iteration
                cur_operation = cur_char    
            
            i += 1  # Main loop counter
        
        return res
