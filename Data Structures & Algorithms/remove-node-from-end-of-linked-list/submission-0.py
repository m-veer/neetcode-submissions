# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast_pointer = head
        is_odd = True
        counter = 0
        while fast_pointer is not None:
            counter += 1
            if fast_pointer.next is None:
                is_odd = True
                break
            elif fast_pointer.next.next is None:
                is_odd = False
                break
            fast_pointer = fast_pointer.next.next
        length = (counter * 2 - 1 if is_odd else counter * 2) if counter > 1 or counter == 1 and ~is_odd else counter

        previous_node = None
        current_node = head
        for index in range(length, 0, -1):
            if index == n:
                if previous_node and current_node.next is not None:
                    previous_node.next = current_node.next
                elif previous_node and current_node.next is None:
                    previous_node.next = None
                elif previous_node is None and current_node.next is not None:
                    head = current_node.next
                else:
                    head = None
                return head
            previous_node = current_node
            current_node = current_node.next