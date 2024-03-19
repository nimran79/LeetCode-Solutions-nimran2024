class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        while(left < right):
            mid = (left + right) // 2

            # If the middle element is greater than its next element,
            # it means a peak element is on the left side(inclusive of mid).
            if nums[mid] > nums[mid + 1]:
                right = mid
            # Otherwise, the peak is in the right half of the array.
            else:
                left = mid + 1
      
        # When left and right pointers meet, we've found a peak element.
        return left
        
        