# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode() # define a new listnode
        head = output # define an empty head for the listnodes
        while list1 and list2: # this loop will run until there's value in list1 or list2
            if list1.val < list2.val: 
                head.next = list1 # if list1 < list2, list1 should be appended to the head node
                list1 = list1.next # since a node of list1 is appended to the head node, we move to the next node in list1
            else:
                head.next = list2 # if list2 < list1, list2 should be appended to the head node
                list2 = list2.next # since a node of list2 is appended to the head node, we move to the next node in list2
            head = head.next # the current head node should always be the latest added node
        head.next = list1 or list2 # if the value of list1 or list2 is null, the while loop would stop, next the node with values should be appended directly to the node list
        return output.next # since our first value was an empty node, we return the next value, which is the first value that we appended to the head list node