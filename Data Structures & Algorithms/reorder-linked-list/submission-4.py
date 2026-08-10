# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:


        dummy = ListNode()
        tail = dummy 
        for j in res:
            tail.next = ListNode(j)
            tail = tail.next 

        return dummy.next


        