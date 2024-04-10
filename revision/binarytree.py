class TreeNode:
    def __init__(self, key, left=None, right=None) -> None:
        self.key = key
        self.left = left
        self.right = right

def create_binary_tree(data):
    if isinstance(data,tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = create_binary_tree(data[0])
        node.right = create_binary_tree(data[2])
    elif data == None:
        node= None
    else:
        node = TreeNode(data)
    return node

tree = create_binary_tree(((1,2,3),2,((1,2,3),3,(1,2,3))))
print(tree.key, tree.left.key, tree.right.key)
