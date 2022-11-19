class Solution:
	def removeNthFromEnd(self, head: Optional[listNode], n: int) -> Optional[listNode]:
        curr = ListNode(0, head)
        left = curr
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return curr.next


head = [1,2,3,4,5]
n = 2
print(Solution(). removeNthFromEnd(head = head , n = n , ))