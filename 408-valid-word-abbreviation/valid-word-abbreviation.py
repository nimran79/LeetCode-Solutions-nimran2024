class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # Initialize pointers for word and abbreviation
        word_index = 0
        abbr_index = 0

        # Loop through the characters in the word and abbr
        while word_index < len(word) and abbr_index < len(abbr):
            if abbr[abbr_index].isdigit():
                cur = 0 
                while abbr_index < len(abbr) and abbr[abbr_index].isdigit():
                    # Leading zero or invalid number check
                    if cur == 0 and abbr[abbr_index] == '0':
                        return False
                    
                    # Calculate the number representing the skipped characters
                    # adjacent substrings are automatically avoided with this calculation 
                    cur = cur * 10 + int(abbr[abbr_index])
                    abbr_index += 1
                word_index += cur  # Move the word index forward by the number of skipped characters
            else:
                if word[word_index] != abbr[abbr_index]:
                    return False
                word_index += 1
                abbr_index += 1
              
        # If we've reached the end of both the word and the abbreviation, the abbreviation is valid
        return word_index == len(word) and abbr_index == len(abbr)
