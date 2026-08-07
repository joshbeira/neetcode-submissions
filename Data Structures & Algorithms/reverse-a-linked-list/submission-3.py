# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            # Save the next node before we overwrite the pointer
            next_node = curr.next 
            
            # Reverse the pointer
            curr.next = prev
            
            # Shift our two pointers forward for the next iteration
            prev = curr
            curr = next_node
            
        # At the end, 'curr' is None, and 'prev' is the new head of the list
        return prev