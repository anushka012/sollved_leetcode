# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        sum_left_leaves = 0
        
        # Check if left child exists and is a leaf node
        if root.left and not root.left.left and not root.left.right:
            sum_left_leaves += root.left.val
        
        # Recursively add left leaves from both left and right subtrees
        sum_left_leaves += self.sumOfLeftLeaves(root.left)
        sum_left_leaves += self.sumOfLeftLeaves(root.right)
        
        return sum_left_leaves