# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        remove = len(nodes) - n
        if remove == 0:
            return head.next
        nodes[remove - 1].next = nodes[remove].next
        return head