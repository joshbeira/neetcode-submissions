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
                if node1.left.val == node2.left.val and node1.right.val == node2.right.val: 
                    continue
                else: 
                    return False 

        return True 
