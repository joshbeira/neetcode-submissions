# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lst = []
        res = []
        while head:
            lst.append(head.val)
            head = head.next

        
        i = 0
        r = len(lst)-1 
        while i < len(lst):
            if i % 2 == 0:
                res.append(lst[i])
            else:
                res.append(lst[r])
                r = r - 1 


            i = i + 1 

        return res

        