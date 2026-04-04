# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # If tree is empty, return empty string
        if not root:
            return ""

        # Initialize result string
        result = ""

        # Initialize queue for level-order traversal
        q = deque()
        q.append(root)

        # Traverse the tree
        while q:
            cur_node = q.popleft()

            if cur_node is None:
                result += "#,"
            else:
                result += str(cur_node.val) + ","
                q.append(cur_node.left)
                q.append(cur_node.right)

        # Return serialized string
        return result
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        # Split the string into node values
        nodes = data.split(",")

        # Create root node
        root = TreeNode(int(nodes[0]))

        # Queue to hold nodes while reconstructing
        q = deque()
        q.append(root)

        # Index to iterate node values
        i = 1

        # Loop through node values
        while q and i < len(nodes) - 1:
            current = q.popleft()

            # Process left child
            if nodes[i] != "#":
                left = TreeNode(int(nodes[i]))
                current.left = left
                q.append(left)
            i += 1

            # Process right child
            if nodes[i] != "#":
                right = TreeNode(int(nodes[i]))
                current.right = right
                q.append(right)
            i += 1

        # Return reconstructed root
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))