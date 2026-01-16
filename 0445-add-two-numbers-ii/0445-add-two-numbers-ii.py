# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        def getDifference(head1, head2):
            len1, len2 = 0, 0
            while head1 or head2:
                if head1:
                    len1 += 1
                    head1 = head1.next
                if head2:
                    len2 += 1
                    head2 = head2.next
            return len1 - len2  
        
        def addTwoNumbershelper(head1,head2):
            
            nonlocal carry

            while not head1 and not head2:
                return 
            addTwoNumbershelper(head1.next,head2.next)
            
            sum = head1.val + head2.val + carry
            
            if sum < 9:
                carry = 0
                head1.val = sum
                return
            else:
                carry = sum // 10
                head1.val = sum % 10
                return
            
            
            
                    
        def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
            nonlocal carry
            head1 = l1
            head2 = l2
            nodeh = None
            node = None
            diff = getDifference(head1, head2)
            while diff != 0: 
                if diff < 0:
                    shorter = True
                    diff+=1 
                    head2 = head2.next
                else:
                    shorter = False
                    diff -= 1
                    head1 = head1.next
                if not node:
                    node = ListNode(0)
                    nodeh = node
                else:
                    node.next = ListNode(0)
                    node = node.next
            
            if nodeh:
                if shorter:
                    node.next = l1
                    l1 = nodeh
                else:
                    node.next = l2
                    l2 = nodeh
                
            addTwoNumbershelper(l1,l2)
            
            if carry == 0:
                return l1
            else:
                extra = ListNode(carry)
                extra.next = l1
                return extra
        
        return add_two_numbers(l1,l2)
                