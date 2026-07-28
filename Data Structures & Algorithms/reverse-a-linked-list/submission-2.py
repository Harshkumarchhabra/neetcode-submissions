# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # testcase:
        # 0,1,2,3,4
        # 0->null
        # 0->1
        # 0->1->2 and repeat

        # Iterative soln:
        # p,c=None,head
        # while c:
        #     temp=c.next
        #     c.next=p #now pointing to prev(p)
        #     p=c
        #     c=temp
        # return p
        
        # recursive:
        if not head:
            return None
        n=head
        if head.next:
            n=self.reverseList(head.next)
            head.next.next=head
        head.next=None
        return n

        