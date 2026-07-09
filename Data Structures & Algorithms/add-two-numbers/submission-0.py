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

        while l1_node and l2_node:
            sum = l1_node.val + l2_node.val + self.carry_forward
            self.carry_forward = 0
            # if (sum:=l1_node.val + l2_node.val + self.carry_forward) > 9:
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
            l1_node, l2_node = l1_node.next, l2_node.next

        post_sum = 0
        if l1_node:
            post_sum = l1_node.val + self.carry_forward
        if l2_node:
            post_sum = l2_node.val + self.carry_forward
        # if self.carry_forward:
            # output.next = ListNode(self.carry_forward)
        if post_sum and post_sum > 9:
            # output.next, output, output.next = ListNode(post_sum % 10), output.next, ListNode(post_sum // 10)
            output.next = ListNode(post_sum % 10)
            output = output.next
            output.next = ListNode(post_sum // 10)
        if self.carry_forward:
            output.next = ListNode(self.carry_forward)
        return output_head