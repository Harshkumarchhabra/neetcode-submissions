# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        list3=node=ListNode()
        while list1 and list2:
            i=list1.val
            j=list2.val
            if i<j:
                node.next=list1
                list1=list1.next
            else:
                node.next=list2
                list2=list2.next
            node=node.next
        
        if list1:
            node.next=list1
        else:
            node.next=list2
        return list3.next