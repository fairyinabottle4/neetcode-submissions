# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None # essentially you set the end of the linked list first
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev # this is the step that reverses the pointer
            prev = curr
            curr = temp
            # the above two steps are iterative steps that move down the list. 
        return prev
        # return prev because it is set to the new head. In effect, it is the last element of the original list.






        