# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # this section calculates the length of the list
        length = 0
        counter = head
        while counter:
            counter = counter.next
            length += 1
        # end of section
        # this section deals with the edge case where the length is 1
        if length == 1:
            head = head.next
            return head
        # end of section
        m = length - n
        curr = head
        prev = None
        # dealing with the edge case where n == length of list
        if m == 0:
            head = head.next
            return head
        # end of section
        while m > 0:
            print(m)
            temp = curr
            curr = curr.next
            prev = temp
            m -= 1
        prev.next = curr.next
        return head
        