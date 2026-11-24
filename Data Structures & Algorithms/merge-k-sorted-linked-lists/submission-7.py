# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None 
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeTwoLists(l1, l2))
            lists = mergedLists
        return lists[0]


    def mergeTwoLists(self, list1, list2):
        res = ListNode()
        curr = res
        while list1 and list2:
            a = list1.val
            b = list2.val
            if a > b:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
            else:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
        if not list1:
            curr.next = list2
        if not list2:
            curr.next = list1
        return res.next

        


        