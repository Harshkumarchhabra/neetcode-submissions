# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # reverse last half 
        # pick one by one
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        dummy=slow.next#start of second half
        slow.next=None#cutting the first half

        prev,cur=None,dummy
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp

        first,dummy=head,prev
        while dummy:
            t1,t2=first.next,dummy.next
            first.next=dummy
            dummy.next=t1
            first,dummy=t1,t2