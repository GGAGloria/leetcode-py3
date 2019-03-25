# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        count = 1
        sum1 = 0
        sum2 = 0
        flag = 0
        if p1.val+p2.val>9:
            flag = 1
            head = ListNode(p1.val+p2.val-10)
        else:
            flag = 0
            head = ListNode(p1.val+p2.val)
        p = head
        
        while(p1!=None and p2!=None):
            if p1.next == None and p2.next == None:
                if flag==0:
                    break
                else:
                    temp = ListNode(1)
                    p.next = temp
                    break
            if p1.next == None and p2.next != None:
                while(p2!=None):
                    if p2.next == None:
                        break
                    p2 = p2.next
                    s = p2.val+flag
                    if s>9:
                        temp = ListNode(s-10)
                        flag = 1
                    else:
                        temp = ListNode(s)
                        flag = 0
                    p.next = temp
                    p = p.next
            elif p1.next != None and p2.next == None:
                while(p1!=None):
                    if p1.next == None:
                        break
                    p1 = p1.next
                    s = p1.val+flag
                    if s>9:
                        temp = ListNode(s-10)
                        flag = 1
                    else:
                        temp = ListNode(s)
                        flag = 0
                    p.next = temp
                    p = p.next      
            else:
                p1 = p1.next
                p2 = p2.next
                s = p1.val+p2.val+flag
                if s>9:
                    flag = 1
                    temp = ListNode(s-10)
                else:
                    flag = 0
                    temp = ListNode(s)
                p.next = temp
                p = p.next
        return head
        
            
        