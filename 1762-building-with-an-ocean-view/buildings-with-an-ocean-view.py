class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # Check if heights array is empty
        if not heights:
          return []
        
        # Initialize an empty list to hold the indices of buildings with an ocean view
        ocean_view_indices = []
      
        # Initialize the maximum height found so far to 0
        max_height = 0
      
        # Iterate from the last building back to the first, range(start,stop, step)
        for i in range(len(heights) - 1, -1, -1):
            # Compare the current building's height with the max height found so far
            if heights[i] > max_height:
                # If the current building is taller, it has an ocean view, So we add its index to our list
                ocean_view_indices.append(i)
                # Update the max_height to the current building's height
                max_height = heights[i]
      
        # The resulting list is in reverse order, so we reverse it before returning
        #  return ocean_view_indices.reverse() # This should also work
        return ocean_view_indices[::-1]
