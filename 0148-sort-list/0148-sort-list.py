# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeTwoSortedList(left,right):
            temp = None
            temph = None
            
            while left or right:
                if not left:
                    if not temp:
                        temp = right
                        temph = temp
                    else:
                        temp.next = right
                        temp = temp.next
                    right = right.next
                elif not right:
                    if not temp:
                        temp = left
                        temph = temp
                    else:
                        temp.next = left
                        temp = temp.next
                    left = left.next
                elif left.val > right.val:
                    if not temp:
                        temp = right
                        temph = temp
                    else:
                        temp.next = right
                        temp = temp.next
                    right = right.next
                else:
                    if not temp:
                        temp = left
                        temph = temp
                    else:
                        temp.next = left
                        temp = temp.next
                    left = left.next
                
            return temph           
        
        def middle_node(head):
            slow = head
            fast = head.next
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow
        
        def sort_list(head):
            if not head or not head.next:
                return head
            
            middle = middle_node(head)
            right = middle.next
            middle.next = None
            left = head
            left = sort_list(left)
            right = sort_list(right)
            
            return mergeTwoSortedList(left,right)
        
        return sort_list(head)