# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #this disconnects head
        temp= head.next
        head=temp

        current = head
        write= ListNode(-1)
        dummyhead= write
        sum=0

        while current:
            if current.val != 0:
                sum+=current.val
                current=current.next
            else:
                write.next= ListNode(sum)
                write= write.next
                sum=0
                current= current.next

        return dummyhead.next

        