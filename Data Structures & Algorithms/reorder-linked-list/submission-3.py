# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow_ptr = head
        length = 0
        while slow_ptr:
            slow_ptr = slow_ptr.next
            length += 1
        mid = (length+1) // 2
        l1 = head
        prev_l2 = head
        l2 = head

        while mid != 0:
            temp = l2
            l2 = l2.next
            prev_l2 = temp
            mid -= 1
            if mid == 0:
                prev_l2.next = None
        # below steps are all for reversing l2
        prev = None
        while l2:
            temp = l2.next
            l2.next = prev
            prev = l2
            l2 = temp
        # l2 sucessfully reversed with prev as it's head
        curr = l1    
        while l1 and prev:
            templ1 = l1.next
            tempprev = prev.next
            curr.next = prev 
            curr = curr.next
            curr.next = templ1
            curr = curr.next
            l1 = templ1
            prev = tempprev


        