# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        curr1 = l1
        curr2 = l2
        while curr1:
            num1 += str(curr1.val)
            curr1 = curr1.next
        while curr2:
            num2 += str(curr2.val)
            curr2 = curr2.next
        num1_rev = num1[::-1]
        num2_rev = num2[::-1]
        add = int(num1_rev) + int(num2_rev)
        add_rev = str(add)[::-1]
        res = ListNode(0)
        curr_res = res
        while add_rev:
            print(add_rev[0])
            num_to_add = int(add_rev[0])
            node_to_add = ListNode(num_to_add)
            curr_res.next = node_to_add
            add_rev = add_rev[1:] 
            curr_res = curr_res.next
        return res.next