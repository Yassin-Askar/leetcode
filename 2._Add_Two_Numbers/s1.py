# Definition for singly-linked list.
Optional = []


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            curr = dummy
            p1, p2 = l1, l2
            carry = 0

            while p1 or p2:
                val1 = p1.val if p1 else 0
                val2 = p2.val if p2 else 0
                s = val1 + val2 + carry
                carry = s // 10
                curr.next = ListNode(s % 10)
                curr = curr.next
                if p1: p1 = p1.next
                if p2: p2 = p2.next

            if carry:
                curr.next = ListNode(carry)

            return dummy.next




l1 = Optional[ListNode]
l2 = Optional[ListNode]
print(Solution(). addTwoNumbers(l1 = l1 , l2 = l2 , ))