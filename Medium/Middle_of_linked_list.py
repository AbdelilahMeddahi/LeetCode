# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_pointer = head
        low_pointer = head       
        while fast_pointer:
            try :
                fast_pointer = fast_pointer.next.next
                low_pointer = low_pointer.next
            except :
                fast_pointer = None
        return low_pointer
        
