# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        x=dummy
        cur=head
        while n>0:
            cur=cur.next
            n-=1#we reached to the point like , length - n th point
        
        while cur:#now we as soon as cur reaches end x will eb at node that we remove 
            x=x.next
            cur=cur.next
        x.next=x.next.next# we move ointer to next node of the one we have to remove
        return dummy.next
