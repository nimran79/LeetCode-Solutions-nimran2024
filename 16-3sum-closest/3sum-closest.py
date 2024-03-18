class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the input array
        closest_sum = float('inf')  # Store the closest sum (initialize with a very large value)

        # range is set so that outer i loop stops at the third-to-last element (-2)
        # This ensures the left and right pointers to always have valid indices
        for i in range(len(nums) - 2):  
            left = i + 1 
            right = len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Update 'closest_sum' if needed
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum

                # Move pointers to find a closer sum
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:  # Found an exact match
                    return closest_sum

        return closest_sum
        