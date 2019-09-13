#problem:https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        a,b=head,head
        for i in range(n+1):
            if not a.next and i!=n:
                return head.next
            
            a=a.next
        while(a!=None):
            b=b.next
            a=a.next
        b.next=b.next.next
        return head
            