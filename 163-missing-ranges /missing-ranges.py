class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        # If nums is empty, return the entire range from lower to upper
        if len(nums) == 0:
            return [[lower, upper]]
      
        # List to store the missing ranges
        missing_ranges = []
      
        # Check if there is a missing range before the start of the array
        if nums[0] > lower:
            missing_ranges.append([lower, nums[0] - 1])
      
        # Loop through the nums array to find ranges
        for i in range(len(nums)-1):
            # If there is a gap greater than one between the two numbers, a missing range is found
            if nums[i+1] - nums[i] > 1:
                missing_ranges.append([nums[i] + 1, nums[i+1] - 1])
      
        # Check if there is a missing range after the end of the array
        if nums[-1] < upper:
            missing_ranges.append([nums[-1] + 1, upper])
      
        # Return the list of missing ranges
        return missing_ranges
