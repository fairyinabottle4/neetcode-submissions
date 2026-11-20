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
        oldToCopy = {None: None} #this deals with the edge case where cur.next is None
        curr = head

        # this chunk copies the nodes into the hashmap, where the key is the object reference to the current node. Note that the node only contains the values, not the pointers
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        # end of chunk

# the key to understanding this question is that you create the hashmap store because you cannot create to pointers to nodes that haven't been created!

        curr = head
        # this chunk inserts the pointers to the nodes in the hash map 
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
        # end of chunk
        return oldToCopy[head]