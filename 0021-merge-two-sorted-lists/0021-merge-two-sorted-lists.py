# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if list1 == None and list2 == None:
            return None
        temp = ListNode(0)
        result = temp
        h1 = list1
        h2 = list2

        while(h1 != None and h2 != None):
            if h1.val < h2.val:
                temp.next = h1
                h1 = h1.next
            else:
                temp.next = h2
                h2 = h2.next
            temp = temp.next
        
        if h1 == None:
            temp.next = h2
        else:
            temp.next = h1
        
        return result.next