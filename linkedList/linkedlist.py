# head = {
#     "value" : 11,
#     "next" : {
#         "value": 4,
#         "next": {
#             "value": 20,
#             "next": {
#                 "value": 30,
#                 "next": None
#             }
#         }
#     }
# }

# # LinkedList Traversal

# linkedListValues = []

# def getValues(ll:dict):
#     linkedListValues.append(ll["value"])
    
#     if ll["next"] == None:
#         return linkedListValues
#     else:
#         return getValues(ll["next"])    

# print(getValues(head))

class LinkedListNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    # create new node
    def __init__(self, value) -> None:
        new_node = LinkedListNode(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # create a node and add it to the end
    def append(self, value) -> bool:
        new_node = LinkedListNode(value)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            self.tail.next = self.tail = new_node
        self.length += 1
        return True
    
    def pop(self) -> LinkedListNode:
        if self.head == None:
            return None
    
        pre = self.head
        temp = self.head
        while temp.next:
            pre, temp = temp, temp.next
        
        self.tail = pre
        self.tail.next = None    
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp.value

    # create a node and add it to the start
    def prepend(self, value) -> None:
        pass
    
    # create a node and insert it at the middle
    def insert(self, index, value) -> None:
        pass

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        

my_linked_list = LinkedList(4)
print(my_linked_list.head)

l1 = LinkedList(10)
# l1.append(20)
# l1.append(30)
l1.print_list()
print("*"*10)
print(l1.pop())
print(l1.pop())
# l1.print_list()
print(l1.pop())
