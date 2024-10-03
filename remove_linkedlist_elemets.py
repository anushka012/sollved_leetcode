# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        current = dummy
        
        # Traverse the list
        while current and current.next:
            # If the next node has the target value, skip it
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        # Return the new head, which is the node after the dummy
        return dummy.next
        