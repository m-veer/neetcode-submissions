# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = list(filter(lambda x: isinstance(x, ListNode), lists))
        if not lists:
            return None
        heap = []

        def return_index(no_of_lists, current_index):
            if current_index + 1 >= no_of_lists:
                return 0
            else:
                return current_index + 1
        current_index = -1
        output = None
        output_node = None
        variable_length = 0
        while True:
            current_index = return_index(len(lists), current_index)

            if len(heap) >= len(lists) - variable_length:
                smallest = heapq.heappop(heap)
                index = smallest[1]
                if not output:
                    # Add this element to the output linked list and move it to next
                    output = ListNode(smallest[0])
                    output_node = output
                    # output_node = output_node.next
                else:
                    # If output linked list is not empty, add the smallest node as next node
                    output_node.next = ListNode(smallest[0])
                    output_node = output_node.next
                current_node = smallest[2]
                if current_node.next is None:
                    lists[index] = None
                    variable_length += 1
                else:
                    heapq.heappush(heap, (current_node.next.val, index, current_node.next))
            else:
                current_node = lists[current_index]
                heapq.heappush(heap, (current_node.val, current_index, current_node))
            
            if not heap:
                break

        return output