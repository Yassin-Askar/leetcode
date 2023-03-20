from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if not node:
                    continue
                if i < size - 1:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root


root = Node()
print(Solution(). connect(root=root, ))
