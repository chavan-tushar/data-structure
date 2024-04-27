class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.length = 1
    
    def print_nodes(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.length > 0:
            new_node.next = self.top
        self.top = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None 
        self.length -= 1
        return temp
    
if __name__ == '__main__':
    s1 = Stack(1)
    s1.push(2)
    s1.push(3)
    s1.push(4)
    s1.push(5)
    s1.print_nodes()
    # s1.pop()
    # s1.pop()
    # s1.pop()
    # s1.pop()
    # s1.pop()
    # s1.pop()
    # s1.pop()
    # s1.pop()
    # s1.push(100)
    # s1.push(200)
    # s1.print_nodes()