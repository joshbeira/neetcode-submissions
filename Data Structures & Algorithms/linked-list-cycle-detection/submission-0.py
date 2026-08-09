# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        lst = []

        while head: 
            lst.append(head.next)
            head = head.next
        
        for i in lst:
            for j in lst: 
                if i == j:
                    return False 
            
        return True 