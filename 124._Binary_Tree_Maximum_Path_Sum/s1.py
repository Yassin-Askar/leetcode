# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            leftMax = max(dfs(root.left), 0)
            rightMax = max(0, dfs(root.right))
            res = max(res, root.val + leftMax+rightMax)
            return root.val + max(leftMax, rightMax)
        dfs(root)
        return res


root = Optional[TreeNode]
print(Solution(). maxPathSum(root=root, ))
