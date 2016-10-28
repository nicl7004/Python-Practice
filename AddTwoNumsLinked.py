# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
   
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        
        while(l1 and l2):
            print(l1.val)
            self.value = (l1.val+l2.val)%10
            l2 = l2.next
            l1 = l1.next
            self = self.next
        
