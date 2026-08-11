# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy node protects us if we need to remove the very first node
        dummy = ListNode(0, head)
        
        # 1. Count total nodes using a temporary pointer (curr)
        total = 0 
        curr = head 
        while curr: 
            total += 1 
            curr = curr.next 

        # 2. Reset our pointer to the dummy node for the second pass
        curr = dummy 
        i = 0 
        
        # 3. Walk to the node EXACTLY BEFORE the one we want to remove
        while i < (total - n): 
            curr = curr.next 
            i += 1 

        # 4. Mutate the list by skipping the target node
        curr.next = curr.next.next 

        # Return the actual head of the list
        return dummy.next