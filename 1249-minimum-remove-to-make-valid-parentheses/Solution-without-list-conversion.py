class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Stack to keep track of characters that lead to a valid string
        stack = []
      
        # Counter to track the balance of parentheses
        open_count = 0
      
        # First pass to remove invalid closing parentheses
        for char in s:
            # If a closing parenthesis is encountered with no matching open, skip it
            if char == ')' and open_count == 0:
                continue
            # If an opening parenthesis is found, increment the open count
            if char == '(':
                open_count += 1
            # If a closing parenthesis is found and there is a matching open, decrement the open count
            elif char == ')':
                open_count -= 1
            # Add the character to the stack as it's part of valid substring so far
            stack.append(char)
      
        # Reset the open counter for the second pass
        open_count = 0
        # List to store the characters for the final answer
        answer = []
      
        # Second pass to remove invalid opening parentheses; process characters in reverse
        for char in reversed(stack):
            # If an opening parenthesis is encountered with no matching close, skip it
            if char == '(' and open_count == 0:
                continue
            # If a closing parenthesis is found, increment the open count
            if char == ')':
                open_count += 1
            # If an opening parenthesis is found and there is a matching close, decrement the open count
            elif char == '(':
                open_count -= 1
            # Add the character to the answer as it is part of a valid substring
            answer.append(char)
      
        # The characters in answer are in reverse order, reverse them back to the correct order
        return ''.join(reversed(answer))
