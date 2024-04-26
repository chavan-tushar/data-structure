class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.before = None

class doubleLinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    
    def append_node(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.tail.next = new_node
            new_node.before = self.tail
            self.tail = new_node
        
        self.length += 1
        return True
    
    def pop_node(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = temp.before
            self.tail.next = None
            temp.before = None 
            
        self.length -= 1
        return temp
    
    def prepend_node(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head 
            self.head = new_node
            self.head.next = temp
            temp.before = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head.next = None
            self.head.before = None
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            temp.next = None
            self.head.before = None
            
        self.length -= 1
        return temp
    
    def get_node(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            # Since doubly linked list has next and before attribute.
            # hence if we have to find a node which is close to the end of the list 
            # then we can start from other end and move backwords.
            if index < self.length // 2:
                temp = self.head
                for _ in range(index):
                    temp = temp.next
            else:
                temp = self.tail
                cnt = 0
                for _ in range(self.length-1, index, -1):
                    temp = temp.before
            return temp
        
    def set_value(self, index, value):
        node = self.get_node(index)
        if node:
            node.value = value
            return True
        return False
    
    def insert_node(self, index, value):
        if index < 0 or index >= self.length:
            return False
        elif index == 0:
            self.prepend_node(value)
        elif index == self.length:
            self.append_node(value)
        else:
            prev_node = self.get_node(index-1)
            next_node = prev_node.next
            new_node = Node(value)

            if prev_node:
                prev_node.next = new_node
                new_node.before = prev_node

            if next_node:
                new_node.next = next_node
                next_node.before = new_node
            self.length += 1
            return True
        
    def remove_node(self,index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            self.pop_first()
        elif index == self.length - 1:
            self.pop_node()
        else:
            temp = self.get_node(index)
            prev = temp.before
            next = temp.next

            temp.next = None
            temp.before = None

            prev.next = next
            next.before = prev
            self.length -= 1
            return True
    
my_doubly_linked_list = doubleLinkedList(7)
my_doubly_linked_list.append_node(14)
my_doubly_linked_list.append_node(21)
my_doubly_linked_list.append_node(28)
my_doubly_linked_list.append_node(35)
my_doubly_linked_list.append_node(42)
my_doubly_linked_list.append_node(49)
my_doubly_linked_list.append_node(56)
my_doubly_linked_list.append_node(63)
my_doubly_linked_list.append_node(70)

my_doubly_linked_list.print_list()

# removedNode = my_doubly_linked_list.pop_node()
# print(f"Succesfully removed Node {removedNode.value}" if removedNode else "No node to remove from list")

# removedNode = my_doubly_linked_list.pop_node()
# print(f"Succesfully removed Node {removedNode.value}" if removedNode else "No node to remove from list")

# # removedNode = my_doubly_linked_list.pop_node()
# # print(f"Succesfully removed Node {removedNode.value}" if removedNode else "No node to remove from list")

# # removedNode = my_doubly_linked_list.pop_node()
# # print(f"Succesfully removed Node {removedNode.value}" if removedNode else "No node to remove from list")

# # removedNode = my_doubly_linked_list.pop_node()
# # print(f"Succesfully removed Node {removedNode.value}" if removedNode else "No node to remove from list")

# my_doubly_linked_list.prepend_node(1)

# my_doubly_linked_list.print_list()

# first_removed_node = my_doubly_linked_list.pop_first()
# print(f"Succesfully removed Node {first_removed_node.value}" if first_removed_node else "No node to remove from list")

# first_removed_node = my_doubly_linked_list.pop_first()
# print(f"Succesfully removed Node {first_removed_node.value}" if first_removed_node else "No node to remove from list")


# my_doubly_linked_list.print_list()

index_num = 7
node_at_index = my_doubly_linked_list.get_node(index_num)
print(f"Value at index {index_num} is {node_at_index.value}" if node_at_index else "Invalid Index")

my_doubly_linked_list.set_value(9, 1999999)
my_doubly_linked_list.insert_node(6,111111)
my_doubly_linked_list.print_list()

my_doubly_linked_list.remove_node(3)
my_doubly_linked_list.print_list()