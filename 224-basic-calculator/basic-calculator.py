class Solution:
    def calculate(self, s: str) -> int:
        stack = []  # Initialize an empty list to be used as a stack
        result, sign = 0, 1  # Initialize result to 0 and sign to 1 ('+' sign)
        index = 0   # Initialize loop counter
      
        # Iterate over the input string
        while index < len(s):
            # If the current character is a digit
            if s[index].isdigit():
                number = 0
                # Continue until a non-digit is found, building the number
                while index < len(s) and s[index].isdigit():
                    number = number * 10 + int(s[index])
                    index += 1
                # Update the result with the current number and the preceding sign
                result += sign * number
                # Compensate for the index increment in the loop
                index -= 1
            
            elif s[index] == "+":   # For a plus, set sign to 1
                sign = 1
            
            elif s[index] == "-":   # For a minus, set sign to -1
                sign = -1
            
            elif s[index] == "(":   # Push the current result and sign to the stack for open parentheses
                stack.append(result)
                stack.append(sign)
                # Reset the result and sign for the new expression within the parentheses
                result, sign = 0, 1
            
            elif s[index] == ")":
                # The result inside the parentheses is multiplied by the sign before the parentheses
                result *= stack.pop()
                # Add the result inside the parentheses to the result before the parentheses
                result += stack.pop()
            
            # Move to the next character
            index += 1
      
        return result  # Return the evaluated result
        