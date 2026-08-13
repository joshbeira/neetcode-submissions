# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 1. Base Case: What do we return if the node doesn't exist?
        if not root:
            return 0
        
        # 2. Traverse down the left and right sides
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # 3. Backtrack: Combine left_depth and right_depth, 
        # and don't forget to count the current node!
        return ...