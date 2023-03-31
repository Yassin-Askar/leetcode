from collections import deque


class Solution:
	def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
		if not root: return []
		q = deque([root])
		res  = []
		direction = 1
		while q:
			level = []
			for _ in range(len(q)):
				node = q.popleft()
				level.append(node.val)
				if node.left:
					q.append(node.left)
				if node.right:
					q.append(node.right)
			res.append(level[::direction])
			direction *= -1
		return res











root = Optional[TreeNode]
print(Solution(). zigzagLevelOrder(root = root , ))