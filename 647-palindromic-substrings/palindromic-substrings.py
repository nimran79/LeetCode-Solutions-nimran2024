class Solution:
    def countSubstrings(self, s: str) -> int:
        n, ans = len(s), 0
        
        # helper function to determine if a substring is a palindrome and 
        # calculate the count of palindromes by expanding from a center point
        def palindromeCount(left: int, right: int) -> int:
            count = 0
            # Expands outwards from the center (left and right) as long as the 
            # characters at those indices match and the indices are within the bounds of the string
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count
        
        for i in range(n):
            even = palindromeCount(i, i + 1)    # even-length palindromes centered between indices i and i + 1
            odd = palindromeCount(i, i)         # odd-length palindromes centered at index
            ans += even + odd
            
        return ans
        