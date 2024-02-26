class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Using a dictionary 'seen' as a hash table
        seen = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = True # Mark the number as seen
        return False
        