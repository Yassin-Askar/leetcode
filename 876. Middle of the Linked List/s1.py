
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
            return head[(len(head)//2)]



i = [1, 2, 3, 4, 5, 2, 5]
print(Solution.middleNode(i))
