# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

     def getData(self):
         return self.data

     def setData(self, newData):
         self.data = newData

     def getNext(self):
         return self.next

     def setNext(self, nextNode):
         self.next = nextNode

class Solution:
# @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next

l1 = ListNode(1)
l1.setNext(2)
l2 = ListNode(2)
l2.setNext(3)
Solution.addTwoNumbers(0,l1,l2)
