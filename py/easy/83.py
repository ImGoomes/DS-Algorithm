# Problem LeetCode 83. Remove  Duplicates from Sorted List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        # 1: Create a list to store unique values and varible to validate last value
        unique = dummy

        if head:
            last_value = head.val
            unique.next = head
            unique = unique.next

        # 2: Loop head
        while head:
            # 3: Validate is last_value is diferent from current value, if so add into the list
            if head.val > last_value:
                unique.next = head
                unique = unique.next
                last_value = head.val
            elif not head.next and head.val == last_value:
                unique.next = None
                unique = unique.next

            head = head.next

        # 4: return unique list
        return dummy.next
