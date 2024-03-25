class TreeNode:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None

# creating 3 nodes of class TreeNode
node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)

# node0 will be root node, node1 will be at its left and node2 will be at its right
node0.left = node1
node0.right = node2

# created a variable tree which will be a binary tree, root node will be node0
tree = node0

print(tree)