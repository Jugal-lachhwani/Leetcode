class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.set = set()

        def helper(node):
            if not node:
                return False
            if k - node.val in self.set:
                return True
            self.set.add(node.val)
            return helper(node.left) or helper(node.right)

        return helper(root)