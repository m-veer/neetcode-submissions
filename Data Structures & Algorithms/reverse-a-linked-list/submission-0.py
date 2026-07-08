# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # We set the current node as the head
        current_node = head

        # Check if the linked list is empty
        if head == None:
            return current_node

        # We set the previous node as None since the first node is supposed to be the last node, further we update the previous node as the current node
        previous_node = None

        # Iterate over the linked list with the current node as head
        while current_node.next is not None:
            # Set the current node's next node as the next node
            next_node = current_node.next

            # Set the previous node as the current node's next node since we are reversing the list
            current_node.next = previous_node

            # Set the current node as the previous node, since we need to link the previous node to reverse the linked list
            previous_node = current_node

            # Set the next node as the current node
            current_node = next_node

        # This is to set the previous node as next node for current node which is the last node
        current_node.next = previous_node
        return current_node