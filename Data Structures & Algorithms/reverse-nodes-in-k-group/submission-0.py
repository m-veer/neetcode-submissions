# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prevGroup=dummy
        def kthElement(curr,k):
            while curr and k>0:
                curr=curr.next
                k-=1
            return curr
        while True:
            kth=kthElement(prevGroup,k)
            if not kth:
                break
            nextGroup=kth.next
            groupStart=prevGroup.next
        #reverse now that we have first and last element
            prev, curr=nextGroup,groupStart
            while curr!= nextGroup:
                tmp=curr.next
                curr.next=prev
                prev=curr
                curr=tmp
            prevGroup.next=kth
            prevGroup=groupStart
        return dummy.next

