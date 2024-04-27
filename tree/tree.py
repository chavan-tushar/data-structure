class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert_node(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root

        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value > temp.value:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp = temp.right
            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                temp = temp.left

    def contains(self, value):
        temp = self.root
        while temp:
            if temp.value == value:
                return True
            elif value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False

if __name__ == '__main__':
    my_tree = BinarySearchTree()
    my_tree.insert_node(10)
    my_tree.insert_node(20)
    my_tree.insert_node(3)
    my_tree.insert_node(4)
    print(f"Root {my_tree.root.value}, Left = {my_tree.root.left.value}, right = {my_tree.root.right.value}, child = {my_tree.root.left.right.value}")
    print(my_tree.contains(4))

