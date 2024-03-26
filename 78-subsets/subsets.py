class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Strategy: Build a decision tree where For each element
        # two paths: in one path include the element in the subset, and in the other, we do not.

        # Helper function using depth-first search to find all subsets
        def depth_first_search(index: int):
            # Base case: Once all elements are considered
            # Make a copy of the current subset (the largest one) and append it to our answer
            if index == len(nums):
                subsets.append(current_subset[:])
                return
          
            # Exclude the current element and move to the next
            depth_first_search(index + 1)
          
            # Include the current element and move to the next
            current_subset.append(nums[index])
            depth_first_search(index + 1)
          
            # Backtrack: remove the current element before going up the recursion tree
            current_subset.pop()

        # This list will hold all the subsets
        subsets = []
        # This is a temporary list to hold the current subset
        current_subset = []
        # Start the depth-first search from index 0
        depth_first_search(0)
        # Return the final list of all subsets
        return subsets
        