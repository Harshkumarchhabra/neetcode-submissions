# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        cur=head
        while cur is not None:
            nex=cur.next#define the next pointer for cur 
            cur.next=prev#set the reverse logic 
            prev=cur#move prev one point forward
            cur=nex#move cur one point forward
        return prev