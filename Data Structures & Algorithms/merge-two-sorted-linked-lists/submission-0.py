# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Store the values of both linked lists in an array
        vals = []
        
        curr1 = list1
        while curr1:
            vals.append(curr1.val)
            curr1 = curr1.next
            
        curr2 = list2
        while curr2:
            vals.append(curr2.val)
            curr2 = curr2.next
            
        # Step 2: Sort the array
        vals.sort()
        
        # Step 3: Convert the sorted array back into a linked list
        dummy = ListNode(-1) # Dummy node to easily return the head later
        current = dummy
        
        for val in vals:
            current.next = ListNode(val)
            current = current.next
            
        return dummy.next