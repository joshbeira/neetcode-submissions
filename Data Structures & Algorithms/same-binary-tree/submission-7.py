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

        while a and b:
            node1 = a.popleft()
            node2 = b.popleft()

            if node1 is None and node2 is None:
                continue

            if node1 is None or node2 is None:
                return False

            if node1.val != node2.val:
                return False

            a.append(node1.left)
            a.append(node1.right)

            b.append(node2.left)
            b.append(node2.right)

        return True
