# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 1. Base Case: If the node is None, its depth is 0
        if not root:
            return 0
        
        # 2. Traverse down the left and right sides
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # 3. Backtrack: Take the longest path and add 1 for the current node
        return max(left_depth, right_depth) + 1