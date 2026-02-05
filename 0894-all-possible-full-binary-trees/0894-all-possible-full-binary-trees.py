# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from functools import lru_cache
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        
        @lru_cache(None)
        def dp(k):
            if k == 1:
                return [TreeNode(0)]
            
            res = []
            for left_size in range(1, k-1, 2):
                if left_size % 2 == 1:
                    right_size = k - 1 - left_size
                    for left in dp(left_size):
                        for right in dp(right_size):
                            node = TreeNode(0)
                            node.left = left
                            node.right = right
                            res.append(node)

            return res
        return dp(n)