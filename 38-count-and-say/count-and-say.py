class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        result = "1"

        for _ in range(n - 1):  # since we already have the first term
            current_char = result[0]
            count = 0
            new_result = ""  # Build the new string

            for char in result:
                if char == current_char:
                    count += 1  # to indicate another occurrence of the same digit
                else:
                    new_result += str(count) + current_char
                    current_char = char
                    count = 1
            
            # Add the last group of digits which wasn't added by the inner loop
            new_result += str(count) + current_char 

            result = new_result  # represents the next term in the sequence
        
        return result
