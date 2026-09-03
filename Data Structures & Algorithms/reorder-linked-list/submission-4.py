# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # mix of reverse and merge and slow and fast 
        slow=head
        fast = head 
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        sec=slow.next
        slow.next=None
        cur=sec
        prev=None
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        # 1 list is till slow and 2nd is prev
        first=head
        scnd=prev
        while scnd:
            t1=first.next
            t2=scnd.next
            first.next=scnd
            scnd.next=t1
            first=t1
            scnd=t2
