# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTInfo:
    def __init__(self, mn, mx, sz):
        self.mini = mn
        self.maxi = mx
        self.mxSz = sz

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxSum = -sys.maxsize
        def largestBSTBT(root):
            if not root:
                return BSTInfo(sys.maxsize, -sys.maxsize, 0)

            left = largestBSTBT(root.left)
            right = largestBSTBT(root.right)

            # Check if the current subtree is a BST
            if left.maxi < root.val and right.mini > root.val:
                self.maxSum = max(root.val + left.mxSz + right.mxSz, self.maxSum)
                return BSTInfo(min(left.mini, root.val),
                            max(right.maxi, root.val),
                            root.val + left.mxSz + right.mxSz)

            return BSTInfo(-sys.maxsize, sys.maxsize, max(left.mxSz, right.mxSz))
        return max(largestBSTBT(root).mxSz,self.maxSum,0)