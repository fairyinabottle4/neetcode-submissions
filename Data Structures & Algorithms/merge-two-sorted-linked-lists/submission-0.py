# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        curr = res
        while list1 and list2:
            a = list1.val
            b = list2.val
            if a > b: # take the smaller value
                curr.next = list2
                list2 = list2.next
                curr = curr.next
            else:
                # b > a
                curr.next = list1
                list1 = list1.next
                curr = curr.next
        # print_linked_list(res)
        if not list1:
            curr.next = list2
        if not list2:
            curr.next = list1
        return res.next

def print_linked_list(head):
    current = head

    while current:
        print(current.val, end=" -> ")
        current = current.next

    print("None")