# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        a = deque([p])
        b = deque([q])
        while p and q: 

            for i in range(len(a)): 
                node1 = a.popleft()
                node2 = b.popleft()
                if node1.left == node2.left and node1.right == node2.right: 
                    continue
                else: 
                    return False 

        return True 
