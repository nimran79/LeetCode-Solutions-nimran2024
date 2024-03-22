class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Since the order of the elements doesn't matter after removal, 
        # you can simply overwrite elements that equal val with elements that do not
        
        # Initialize a new index for the updated list without the value 'val'
        new_length = 0 

        # Iterate over each number in 'nums' to put valid elements at the front of 'nums'
        for number in nums:
            # If the current number is not the value to remove, update the list
            if number != val:
                # Assign the number to the new index location
                nums[new_length] = number
                # Increment the new length to move to the next index
                new_length += 1

        # Return the new length of the list after all removals are completed
        return new_length