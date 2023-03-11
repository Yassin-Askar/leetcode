
# ! time O(N)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return [0, 0]
            left = dfs(root.left)
            right = dfs(root.right)

            with_root = root.val + left[1] + right[1]
            no_root = max(left) + max(right)
            return [with_root, no_root]
        return max(dfs(root))
