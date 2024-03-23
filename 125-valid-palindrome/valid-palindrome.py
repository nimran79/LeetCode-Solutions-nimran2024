class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Pointers at the start and end of the string.
        left, right = 0, len(s) - 1
      
        while left < right:
            # Skip non-alphanumeric characters by moving the left pointer forward.
            if not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric characters by moving the right pointer backward.
            elif not s[right].isalnum():
                right -= 1
            # If the characters are alphanumeric and do not match, it's not a palindrome.
            elif s[left].lower() != s[right].lower():
                return False
            # If characters at the current pointers match, move both pointers towards center.
            # Don't need lowercase for s[left] == s[right] since we are only moving pointer
            else:
                left += 1
                right -= 1
      
        # If we haven't found any mismatches at the end (left=right), then it's a palindrome.
        return True