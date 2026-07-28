# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s=head
        f=head
        while f and f.next:
            s=s.next
            f=f.next.next
        second=s.next
        prev=s.next=None
        while second:
            nxt=second.next#initialize
            second.next=prev#reverse
            prev=second#update
            second=nxt#update
        first,second=head,prev
        while second:
            nxt1,nxt2=first.next,second.next
            first.next=second
            second.next=nxt1#becasue we are inserting second'th node in b/s first and first.next
            first,second=nxt1,nxt2
        