# Solution using HashMap
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Count the occurrences of each character in the string s
        s_count = collections.Counter(s)

        # Initialize the answer as an empty list; it will store the sorted characters
        sorted_characters = []

        # Add characters to the sorted_characters list following the order specified.
        # Multiply the character by its count to add it that many times.
        for char in order:
            sorted_characters.append(char * s_count[char])
            # Set the count for this character to 0 since it's been added in ans (using char as key)
            s_count[char] = 0

        # Add remaining characters that were not in 'order' to the list.
        # These are added at the end in their original order of occurrence.
        for char, count in s_count.items():
            sorted_characters.append(char * count)

        # Join all the characters in the sorted_characters list to form the sorted string
        return ''.join(sorted_characters)
        
