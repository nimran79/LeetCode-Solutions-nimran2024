# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Helper function to perform depth-first search.
        def dfs(node, num_sum):
            # If the current node is None, we've reached a leaf or the tree is empty.
            if not node:
                return 0
          
            # Update the sum for the current path: 
            # previous sum times 10 plus the current node's value since digits are 0~9.
            num_sum = num_sum * 10 + node.val
          
            # If we're at a leaf node, return the current sum.
            if not node.left and not node.right:
                return num_sum
          
            # Continue the depth-first search on left and right subtrees, adding their sums.
            return dfs(node.left, num_sum) + dfs(node.right, num_sum)
      
        # Start the dfs with the root node and an initial sum of 0.
        return dfs(root, 0)
        