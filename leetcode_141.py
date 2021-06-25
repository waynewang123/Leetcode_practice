# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        ##快慢指针，一个一次1步，一个1次2步，看最终是否会相遇
        if head is None:
            return False
        slow = head
        fast = head
        while (fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
