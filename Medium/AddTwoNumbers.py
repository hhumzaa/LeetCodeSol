# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Time complexity: O(MAX(m,n)) where m, n are the size of l1 and l2, this is due to checking 
    all nums in the longest list
    Space complexity: O(MAX(m,n) as the result list is the size of the longest list + 1 if carry over
    """
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        emptyNode = ListNode()
        curr = emptyNode

        while l1 is not None or l2 is not None or carry != 0:
            total = carry

            if l1 is not None:
                total = total + l1.val
                l1 = l1.next

            if l2 is not None:
                total = total + l2.val
                l2 = l2.next
            
            num = total % 10
            carry = total // 10

            curr.next = ListNode(num)
            curr = curr.next

        return emptyNode.next
