class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # using Set's inherent property to store unique elements
        return len(set(nums)) != len(nums)
        