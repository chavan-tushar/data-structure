
class TreeNode():
    def __init__(self, key) -> None:
        self.key = key
        self.right = None
        self.left = None

node0 = TreeNode(2)
node1 = TreeNode(3)
node2 = TreeNode(5)
node3 = TreeNode(1)
node4 = TreeNode(3)
node5 = TreeNode(7)
node6 = TreeNode(4)
node7 = TreeNode(6)
node8 = TreeNode(8)

# creating tree manually
tree1 = node0
node0.left = node1
node0.right = node2

node1.left = node3
node2.left = node4
node2.right = node5

node4.right = node6
node5.left = node7
node5.right = node8

# creating binary tree through function using tuple
def parse_tuple(data):
    # print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

tree2 = parse_tuple(((1,3,None), 2, ((None, 3, 4),5,(6,7,8))))
print(tree2.right.key)

def tree_to_tuple(node:TreeNode) -> tuple[tuple]:
    if isinstance(node, TreeNode):
        if node.left is None and node.right is None:
            return node.key
        
        return(
            tree_to_tuple(node.left),
            node.key, 
            tree_to_tuple(node.right)
        )
  

print(tree_to_tuple(tree2))

def display_keys(node, space="\t", level=0):
    # if node is None
    if node is None:
        print(space*level + "@")
        return
    
    # if node is a leaf
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    
    # if node has a children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left, space, level+1)

display_keys(tree2,"    ")


def binary_tree_treversal_in_order(tree:TreeNode) -> list[int]:
    if tree is None:
        return []
    else:
        return (
            binary_tree_treversal_in_order(tree.left)+ [tree.key] + binary_tree_treversal_in_order(tree.right)
        )

print(binary_tree_treversal_in_order(tree2))

def binary_tree_treversal_pre_order(tree:TreeNode) -> list[int]:
    if tree is None:
        return []
    else:
        return (
            [tree.key] + binary_tree_treversal_in_order(tree.left) + binary_tree_treversal_in_order(tree.right)
        )

print(binary_tree_treversal_pre_order(tree2))


def binary_tree_treversal_post_order(tree:TreeNode) -> list[int]:
    if tree is None:
        return []
    else:
        return (
            binary_tree_treversal_in_order(tree.left) + binary_tree_treversal_in_order(tree.right) + [tree.key]
        )

print(binary_tree_treversal_post_order(tree2))

def binary_tree_height(node):
    if node is None:
        return 0
    return 1 + max(binary_tree_height(node.left), binary_tree_height(node.right))

print(f"Height of the Binary tree is {binary_tree_height(tree2)}")

def binary_tree_size(node):
    if node is None:
        return 0
    return 1 + binary_tree_size(node.left) + binary_tree_size(node.right)

print(f"Size of the Binary tree is {binary_tree_size(tree2)}")