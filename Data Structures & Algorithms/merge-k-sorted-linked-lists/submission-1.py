# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        
        # Step 1: Traverse all linked lists and add their contents to an array
        for linked_list in lists:
            while linked_list:
                nodes.append(linked_list.val)
                linked_list = linked_list.next
                
        # Step 2: Sort the array
        nodes.sort()
        
        # Step 3: Turn the sorted array back into a linked list
        dummy = ListNode(0)
        current = dummy
        for val in nodes:
            current.next = ListNode(val)
            current = current.next
            
        return dummy.next