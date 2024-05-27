# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import gcd
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        while head.next:
            tmp = ListNode()
            tmp.next = head.next
            tmp.val = gcd(head.val,head.next.val)
            head.next = tmp
            head  = head.next.next
        return start
