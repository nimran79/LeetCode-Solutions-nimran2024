# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:    # Tree is empty
            return False
        
        if not root.left and not root.right:    # leaf node
            return root.val == targetSum 
        
        # Recursive call
        left_sum = self.hasPathSum(root.left, targetSum - root.val)
        right_sum = self.hasPathSum(root.right, targetSum - root.val)
        
        # Having one of left or right subtree valid path is enough
        return left_sum or right_sum
        