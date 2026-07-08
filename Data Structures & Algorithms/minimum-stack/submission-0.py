class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MinStack:
    def __init__(self):
        self.head = None
        self.minimum = None
    def push(self, val: int) -> None:
        if self.head is None:
            self.head = ListNode(0)
            self.minimum = val
        else:
            temporary_head = self.head
            self.head = ListNode(val - self.minimum)
            self.minimum = val if val < self.minimum else self.minimum
            self.head.next = temporary_head

    def pop(self) -> None:
        self.minimum = self.minimum - self.head.val if self.head.val < 0 else self.minimum
        self.head = self.head.next

    def top(self) -> int:
        top = self.head.val
        if top > 0:
            return top + self.minimum
        else:
            return self.minimum

    def getMin(self) -> int:
        return self.minimum