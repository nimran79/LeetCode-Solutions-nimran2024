# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both trees are None, they are the same (both empty)
        if p == q:
            return True
      
        # If one of the trees is None or the values of current nodes are different,
        # then the trees are not the same.
        if p is None or q is None or p.val != q.val:
            return False
      
        # Otherwise, check recursively for the left and right subtrees.
        # Both subtrees must be the same for the entire trees to be considered the same.
        return self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)
        