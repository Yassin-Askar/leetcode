from tkinter.tix import ListNoteBook
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNoteBook]) -> Optional[ListNoteBook]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr and curr.next:
            next_pair = curr.next.next
            second_node = curr.next

            second_node.next = curr
            curr.next = next_pair
            prev.next = second_node

            prev = curr
            curr = next_pair
        return dummy.next


head = None
print(Solution(). swapPairs(head=head, ))
