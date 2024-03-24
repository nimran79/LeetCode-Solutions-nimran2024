class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store numbers and their indices
        hashmap = {}

        for i, number in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - nums[i]
            
            # If complement is in the index_map, a solution is found
            if complement in hashmap:
                return [i, hashmap[complement]]
            # Otherwise, add the current number and its index to the index_map
            hashmap[number] = i

        # Since the problem guarantees exactly one solution, the loop should never finish without returning
        