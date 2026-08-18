# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root: return True 
        if not subRoot: return False 

        if self.sameTree(subRoot,root):
            return True 

        return (self.isSubtree(subRoot.left, root) or 
        self.isSubtree(subRoot.right, root))


        def sameTree(self, s, t): 
            if not s and not t: 
                return True 
            if not s or not t or s.val != t.val: 
                return False 

            return(self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)) 