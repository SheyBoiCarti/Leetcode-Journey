# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2

        if list2 is None:
            return list1

        dummynode= ListNode(-1)
        dummyhead= dummynode

        l1= list1
        l2=list2

    
        while(l1 is not None and l2 is not None):
            if l1.val <= l2.val:
                dummynode.next= ListNode(l1.val)
                dummynode= dummynode.next
                l1= l1.next

            elif l1.val > l2.val:
                dummynode.next= ListNode(l2.val)
                dummynode= dummynode.next
                l2= l2.next
            
            if l1 is None:
                dummynode.next= l2
                return dummyhead.next
            
            if l2 is None:
                dummynode.next= l1
                return dummyhead.next
        
        return dummyhead.next
            