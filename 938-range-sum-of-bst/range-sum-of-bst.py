# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if node:
                 # If the current node's value is within the range [low, high], add it to the total sum
                if low <= node.val <= high:
                    self.total_sum += node.val
                # If the current node's value is greater than the low value of the range
                # then search to the left as all right values will also be greater
                if low < node.val:
                    dfs(node.left)
                # If the current node's value is less than the high value of the range
                # then search to the right as all left values will also be less
                if node.val < high:
                    dfs(node.right)

        self.total_sum = 0
        dfs(root)
        return self.total_sum
