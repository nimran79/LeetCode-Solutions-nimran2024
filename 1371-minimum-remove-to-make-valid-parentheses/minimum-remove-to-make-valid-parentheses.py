class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Convert string to list to make operations easier
        s = list(s)
        # Stack to keep track of characters that lead to a valid string
        stack = []

        for i, char in enumerate(s):
            # For open parenthesis we add an index to the stack
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop() # For close parenthesis we pop an index from the stack
                else:
                    s[i] = ''   # when stack is empty (more ')' than '(' in s)
        
        # replace all indices with '' stored in stack, since these opening '(' don't have close ')'
        while stack:
            s[stack.pop()] = ''

        # Convert list back to string
        return ''.join(s)