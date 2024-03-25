# Assuming NestedInteger class definition exists (as provided in the problem description)

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nested_list, current_depth):
            current_depth_sum = 0  # Initialize the depth sum for the current level

            # Loop through each item in the current nested list
            for item in nested_list:
                if item.isInteger():
                    # If the item is an integer, add its value times the current depth
                    current_depth_sum += item.getInteger() * current_depth
                else:
                    # If the item is a list, recursively call dfs to calculate its depth sum
                    current_depth_sum += dfs(item.getList(), current_depth + 1)
          
            return current_depth_sum  # Return the calculated depth sum for this level

        # Start the Recursion with the main top-level list and depth 1
        return dfs(nestedList, 1)
