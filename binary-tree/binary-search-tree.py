# A binary search tree is a binary tree which satisfies below conditions,
# 1. The left subtree of any node only contains nodes with keys less than the node's value
# 2. The right subtree of any node only contains the nodes with keys greater than the node's value. 
# Every subtree should fullfil above conditions to be a binary search tree.

class TreeNode():
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    @staticmethod
    def parse_tuple(data:tuple):
        # print(data)
        if isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        elif data is None:
            node = None
        else:
            node = TreeNode(data)
        return node


def remove_none(nums):
    return [x for x in nums if x is not None]


def is_binary_search_tree(node) -> bool:
    if node is None:
        return True, None, None
    
    is_bst_l, min_l, max_l = is_binary_search_tree(node.left)
    is_bst_r, min_r, max_r = is_binary_search_tree(node.right)

    is_bst_node = (is_bst_l and is_bst_r and 
                (max_l is None or node.value > max_l) and
                (min_r is None or node.value < min_r))
    
    min_key = min(remove_none([min_l, node.value, min_r]))
    max_key = max(remove_none([max_l, node.value, max_r]))

    return is_bst_node, min_key, max_key


tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))
tree = TreeNode.parse_tuple(tree_tuple)

user_tuple = (("aakash","biraj","hemanth"), "jadesh", ("siddhant","sonaksh","vishal"))
user_tree = TreeNode.parse_tuple(user_tuple)


# storing a key value pair using BSTs
class BSTNode():
    def __init__(self, key, value=None) -> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

# tree = BSTNode(jadhesh.username, jadhesh)






            

            

