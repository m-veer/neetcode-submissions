class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isValid(self, s: str) -> bool:
        mapping_dictionary = {
            "]": "[",
            "}": "{",
            ")": "("
        }
        head = None
        for character in s:
            if not head:
                head = ListNode(character)
            else:
                if character in mapping_dictionary.keys() and head.val == mapping_dictionary.get(character):
                    head = None if not head.next else head.next
                else:
                    temp = head
                    head = ListNode(character)
                    head.next = temp
        return head is None