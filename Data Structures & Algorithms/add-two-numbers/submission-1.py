# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        self.carry_forward = 0
        l1_node, l2_node = l1, l2
        output = None
        while l1_node or l2_node or self.carry_forward:
            l1_node_value = l1_node.val if l1_node else 0
            l2_node_value = l2_node.val if l2_node else 0

            # sum = l1_node.val + l2_node.val + self.carry_forward
            sum = l1_node_value + l2_node_value + self.carry_forward
            self.carry_forward = 0
            if sum > 9:
                if not output:
                    output = output_head = ListNode(sum % 10)
                else:
                    output.next = ListNode(sum % 10)
                    output = output.next
                self.carry_forward += sum // 10
            else:
                if not output:
                    output = output_head = ListNode(sum)
                else:
                    output.next = ListNode(sum)
                    output = output.next
            if l1_node:
                l1_node = l1_node.next
            if l2_node:
                l2_node = l2_node.next
            # l1_node, l2_node = l1_node.next, l2_node.next
        return output_head