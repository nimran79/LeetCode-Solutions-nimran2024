class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # initialize an empty list to store the triplets
        result = []

        # sort the list in ascending order
        nums.sort()

        # Main Loop
        for i in range(len(nums)):
            # Not to reuse the same 1st value
            if i>0 and nums[i] == nums[i-1]:
                continue

            # two pointer solution
            left, right  = i+1, len(nums)-1

            while(left < right):
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum > 0:    # result too big, need to decrease sum
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:   # Valid sum
                    result.append([nums[i], nums[left], nums[right]])   # add as a list
                    # Increment left pointer to find the next valid sum
                    left += 1
                    while(nums[left] == nums[left-1] and left < right):
                        left += 1   # Not to use duplicate
        return result
        