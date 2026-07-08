# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLinkedList(self, head):
        current_node = head
        previous_node = None
        while current_node.next is not None:
            next_ndoe = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_ndoe
        current_node.next = previous_node
        reversed_linked_list = current_node
        return reversed_linked_list
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Approach
        # Split the lists based on the middle
        # Reverse the second half of the list
        # Merge by adding the second list elements in the first in between

        # Split the linked list
        # if head.next is None:
            # return head
            # self.printLinkedList(head)
        if head.next:
            slow_pointer = head
            fast_pointer = head
            first_half = head
            second_half = head
            while fast_pointer is not None:
                if fast_pointer.next is None or fast_pointer.next.next is None:
                    second_half = slow_pointer.next
                    slow_pointer.next = None
                    break
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next.next

            # Reverse the second half of the linked list
            reversed_second_half = self.reverseLinkedList(second_half)

            # Merge the two linked lists:
            output = None
            is_first_half = True
            while first_half or reversed_second_half:
                if not output:
                    output = first_half
                    first_half = first_half.next
                else:
                    output.next = first_half if is_first_half else reversed_second_half
                    output = output.next
                    if is_first_half:
                        first_half = first_half.next
                    else:
                        reversed_second_half = reversed_second_half.next
                is_first_half = not is_first_half
            # return head
        else:
            pass