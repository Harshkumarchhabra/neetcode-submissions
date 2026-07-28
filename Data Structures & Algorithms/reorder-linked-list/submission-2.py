# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [2,4,6,8]
        # 2,4 
        # 8,6
        # 2,8,4,6,
        s,f=head,head
        while f and f.next:
            s=s.next
            f=f.next.next
        scnd=s.next#reached half point
        prev=s.next=None
        while scnd:#reversing scnd half
            nxt=scnd.next
            scnd.next=prev
            prev=scnd
            scnd=nxt
        
        frst,scnd=head,prev
        while scnd:#joining first half and reversed secnd half
            x,y=frst.next,scnd.next
            frst.next=scnd
            scnd.next=x
            frst,scnd=x,y

