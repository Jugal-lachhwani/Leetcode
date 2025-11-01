# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, n: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        n = set(n)
        while head and head.val in n:
            head = head.next
        temp = head

        while temp.next:
            if temp.next.val in n:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return head