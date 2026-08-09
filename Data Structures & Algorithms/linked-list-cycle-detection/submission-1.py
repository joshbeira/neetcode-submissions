# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        
        while head:
            # If we've seen this exact node before, we're in a loop
            if head in seen:
                return True
                
            # Otherwise, add it to our history and move forward
            seen.add(head)
            head = head.next
            
        # If we hit None, there is an end to the list (no cycle)
        return False