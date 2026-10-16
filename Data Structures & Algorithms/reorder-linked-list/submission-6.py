# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        cur=slow.next
        slow.next=None
        prev,cur2=None,cur
        while cur2:
            temp=cur2.next
            cur2.next=prev
            prev=cur2
            cur2=temp
        first,second=head,prev
        while second:
            t1,t2=first.next,second.next
            first.next=second
            second.next=t1
            first=t1
            second=t2