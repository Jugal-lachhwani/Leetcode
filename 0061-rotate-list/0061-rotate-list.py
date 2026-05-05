# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        l = 1
        temp = head
        while temp.next:
            temp = temp.next
            l+=1
        last = temp
        if l > k:
            pass
        else:
            k = k % l 
        if k == 0:
            return head
        r = l - k - 1
        temp = head
        while temp and r > 0:
            temp = temp.next
            r -= 1
        print(temp.val,last.val)
        new_head = temp.next
        temp.next = None
        last.next = head
        return new_head


