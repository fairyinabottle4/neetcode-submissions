# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None 
        mergedLists = []
        while len(lists) > 1:
            list1, list2 = lists.pop(), lists.pop()
            res = self.mergeTwoLists(list1, list2)
            mergedLists.append(res)
        if len(lists) == 1:
            mergedLists.append(lists[0])
                
        while len(mergedLists) > 1:
            newLists = []

            for i in range(0, len(mergedLists) - 1, 2):
                l1 = mergedLists[i]
                l2 = mergedLists[i + 1]
                newLists.append(self.mergeTwoLists(l1, l2))

            # Handle the odd leftover list
            if len(mergedLists) % 2 == 1:
                newLists.append(mergedLists[-1])

            mergedLists = newLists

        return mergedLists[0]
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

        


        