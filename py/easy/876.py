# Problem LeetCode 876. Midddle of the Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ahead = head

        while ahead and ahead.next:
            ahead = ahead.next.next
            head = head.next

        return head
