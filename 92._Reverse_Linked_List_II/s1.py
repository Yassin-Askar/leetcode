class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: listNode, left: int, right: int) -> listNode:
        dummy = ListNode(0, head)
        left_prev, cur = dummy, head
        for _ in range(left - 1):
            left_prev, cur = cur, cur.next

        prev = None
        for _ in range(right-left + 1):
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp
        left_prev.next.next = cur
        left_prev.next = prev

        return dummy.next


head = ListNode(0)
left = 1
right = 5
print(Solution(). reverseBetween(head=head, left=left, right=right, ))
