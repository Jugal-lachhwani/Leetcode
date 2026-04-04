# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        # Initialize a pointer
        # 'curr' to the root of the tree
        curr = root

        # Iterate until 'curr'
        # becomes None
        while curr:
            if curr.left:
                pre = curr.left
                while pre.right:
                    pre = pre.right

                # Connect the rightmost node in
                # the left subtree to the current
                # node's right child
                pre.right = curr.right

                # Move the entire left subtree to the
                # right child of the current node
                curr.right = curr.left

                # Set the left child of
                # the current node to None
                curr.left = None

            # Move to the next node
            # on the right side
            curr = curr.right
        return root
        