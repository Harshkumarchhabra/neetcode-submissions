# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,cur=None,head
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        #2,6,3,7,4
        dummy=prev
        while dummy.next:
            if dummy.val>dummy.next.val:
                dummy.next=dummy.next.next
            else:
                dummy=dummy.next
        prev1,cur1=None,prev
        while cur1:
            temp=cur1.next
            cur1.next=prev1
            prev1=cur1
            cur1=temp
        return prev1