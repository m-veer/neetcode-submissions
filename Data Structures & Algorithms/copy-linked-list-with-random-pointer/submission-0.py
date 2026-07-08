"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        random_pointers = {}

        copy_random_list_head = None
        copy_random_list = None

        current_node = head
        index = 0
        # previous_node = None
        while current_node is not None:
            temporary_node = Node(current_node.val, None, None)
            # previous_node = temporary_node

            if not copy_random_list:
                copy_random_list_head = temporary_node
                copy_random_list = temporary_node
            else:
                copy_random_list.next = temporary_node
                copy_random_list = copy_random_list.next

            # random_pointers[index] = {
            #     "node" : current_node,
            #     "val" : current_node.val,
            #     "next" : None if not current_node.next else current_node.next,
            #     "random" : None if not current_node.random else current_node.random
            # }
            # random_pointers[current_node] = None if not current_node.random else current_node.random
            # random_pointers[None if not current_node.random else current_node.random] = {"index": index, "current_node" : current_node}
            # random_pointers[current_node] = {"index": index, "current_node" : None if not current_node.random else current_node.random, "new_node" : temporary_node}

            random_pointers[current_node] = {
                "index": index,
                # "current_node" : current_node,
                "random_node" : None if not current_node.random else current_node.random,
                "new_node" : temporary_node
                }
            current_node = current_node.next
            index += 1

        # print(random_pointers)

        # pointers = {}
        # index = 0
        # for key, value in random_pointers.items():
        #     # print(key, value)
        #     # if key:
        #     #     pointers[key] = random_pointers.get(value['current_node'])["index"]
        #     # else:
        #     #     pointers[key] = value["index"]
        #     if value['current_node']:
        #         pointers[index] = random_pointers[value['current_node']]['index']
        #     else:
        #         pointers[index] = None
        #     index += 1
        
        # current_node = copy_random_list_head
        # index = 0
        # while current_node is not None:
        #     # current_node.random = random_pointers[index['current_node']]['new_node']
        #     random_pointer = random_pointers[index]['random_node']
        #     # current_node.random = None if random_pointer is None else random_pointers[index]['new_node']
        #     current_node.random = random_pointers[index]['new_node'] if random_pointer else random_pointers[index]['new_node']
        #     current_node = current_node.next
        #     index += 1
        
        current_node = copy_random_list_head
        for _, value in random_pointers.items():
            random_node = value['random_node']
            current_node.random = random_pointers[random_node]['new_node'] if random_node is not None else None
            current_node = current_node.next

        # current_node = copy_random_list_head
        # index = 0
        # while current_node is not None:
        #     if not pointers[index]:
        #         current_node.random = 
        #     index += 1
        return copy_random_list_head