# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Remove the nodes which won't be reversed
        # Reverse the whole linkedlist and then connect the required nodes

        # Checking the number of nodes
        current = head
        length = 1
        while current.next is not None:
            if current.next and current.next.next:
                current = current.next.next
                length += 2
            elif current.next:
                current = current.next
                length += 1

        # Get the number of splits
        no_of_splits = length//k
        
        current = head
        prev = None
        start = None
        output = None
        for index in range(no_of_splits):
            end = start
            start = current
            for _ in range(k):
                next = current.next
                current.next = prev

                prev = current
                current = next

            if not index:
                start.next = current
                output = prev
            else:
                start.next = current
                end.next = prev
        return output

