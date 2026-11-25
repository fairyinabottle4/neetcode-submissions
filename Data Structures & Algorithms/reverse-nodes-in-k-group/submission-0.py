# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        group_end = None
        new_head = None
        new_head_set = False
        # This section is purely to find the length of the list
        length = 0
        while curr:
            length += 1
            curr = curr.next
        curr = head
        iterations = length // k
        # end of section
        while iterations > 0:
            prev = None
            k_copy = k
            group_start = curr
            while k_copy > 0:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                k_copy -= 1
            if not new_head_set:
                new_head = prev
                new_head_set = True
            if group_end is not None:
                group_end.next = prev
            group_end = group_start
            group_start.next = curr
            iterations -= 1
        return new_head


        