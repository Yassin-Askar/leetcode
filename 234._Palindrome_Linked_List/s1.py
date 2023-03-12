
class ListNode:
    def __init__(self, val=0, next=None):
        self.data = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        left = head
        right = prev
        while right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next
        return True


# ! [1,2,2,1]
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(2)
# head.next.next.next = ListNode(1)

head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)
# ! [1,2,2,2,1]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)
print(Solution(). isPalindrome(head=head, ))
