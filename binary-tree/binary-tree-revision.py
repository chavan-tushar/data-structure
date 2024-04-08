class TreeNode():
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

node0 = TreeNode(2)
node1 = TreeNode(3)
node2 = TreeNode(5)
node3 = TreeNode(1)
node4 = TreeNode(3)
node5 = TreeNode(7)
node6 = TreeNode(4)
node7 = TreeNode(6)
node8 = TreeNode(8)

def create_tree(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = create_tree(data[0])
        node.right = create_tree(data[2])
    elif data == None:
        node = None
    else:
        node = TreeNode(data)
    return node

tree2 = create_tree(((1,3,None), 2, ((None, 3, 4),5,(6,7,8))))
print(tree2.value)


def tree_to_tuple(treeNode: TreeNode) -> tuple:
    if isinstance(treeNode, TreeNode):
        if treeNode.left is None and treeNode.right is None:
            return treeNode.value
        return (tree_to_tuple(treeNode.left), treeNode.value, tree_to_tuple(treeNode.right))
        
    
print(tree_to_tuple(tree2))

def print_tree(treeNode: TreeNode, space="\t", level=0):
    if treeNode is None:
        print(space*level + "@")
        return
    
    if treeNode.left is None and treeNode.right is None:
        print(space*level + str(treeNode.value))
        return
    
    print_tree(treeNode.right, space, level+1)
    print(space*level + str(treeNode.value))
    print_tree(treeNode.left, space, level+1)

print_tree(tree2, "     ")


def in_order_traversal(treeNode: TreeNode) -> list:
    if treeNode is None:
        return []
    return (in_order_traversal(treeNode.left) + [treeNode.value] + in_order_traversal(treeNode.right))

print("In order Traversal", in_order_traversal(tree2))

def pre_order_traversal(treeNode: TreeNode) -> list:
    if treeNode is None:
        return []
    return ([treeNode.value] + pre_order_traversal(treeNode.left) + pre_order_traversal(treeNode.right))

print("Pre order Traversal", pre_order_traversal(tree2))

def post_order_traversal(treeNode: TreeNode) -> list:
    if treeNode is None:
        return []
    return (post_order_traversal(treeNode.left) + post_order_traversal(treeNode.right)+[treeNode.value])

print("Post order Traversal", post_order_traversal(tree2))