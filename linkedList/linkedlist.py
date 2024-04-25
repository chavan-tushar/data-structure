class linkedListNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value) -> None:
        node = linkedListNode(value)
        self.head = node
        self.tail = node
        self.count = 1
        
    def append_element(self, value) -> None:
        node = linkedListNode(value)
        self.tail.next = node
        self.tail = node
        self.count += 1
    
    def printNode(self):
        print(f"Below are all the nodes of Linked List. The size is {self.count}")
        currentNode = self.head

        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.next

    def pop_element(self) -> int:
        prevNode = None
        currentNode = self.head
        if self.count == 0:
            return None
        elif self.count == 1:
            self.head = self.tail = None
        else:    
            while currentNode.next:
                prevNode, currentNode = currentNode, currentNode.next
            self.tail = prevNode
            self.tail.next = None
        self.count -= 1
        return currentNode.value
    
    def prepend(self,value):
        node = linkedListNode(value)
        if self.count == 0:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.count += 1
        return True
    
    def popFirst(self):
        if self.count == 0:
            return None
        elif self.count == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        self.count -= 1
        return True
    
    def get_value(self,index) -> linkedListNode:
        if index < 0 or index >= self.count:
            return None
        else:
            cnt = 0
            temp = self.head
            while cnt < index:
                temp = temp.next
                cnt += 1
            return temp.value
        
    def set_value(self, index, value):
        if index < 0 or index >= self.count:
            return None
        else:
            temp = self.head
            for _ in range(1, index+1):
                temp = temp.next
            temp.value = value
    
    def insert_value(self, index, value):
        
        if index < 0 or index > self.count:
            return None
        elif index == 0:
            self.prepend(value)
        elif index == self.count:
            self.append_element(value)
        else:
            node = linkedListNode(value)
            temp = self.head
            for i in range(1, index):
                temp = temp.next
            tempNext = temp.next
            temp.next, node.next = node, tempNext
            self.count += 1

if __name__ == '__main__':


    ll = LinkedList(4)

    for i in range(100,201,25):
        ll.append_element(i)

    print(f"Head is {ll.head.value}, Tail is {ll.tail.value}, and total items in Linked list are {ll.count}")

    # ll.printNode()
    # removedNode = ll.pop()
    # print(f"Successfully removed {removedNode}")
    # removedNode = ll.pop()
    # print(f"Successfully removed {removedNode}")
    # removedNode = ll.pop()
    # print(f"Successfully removed {removedNode}")
    # removedNode = ll.pop()
    # print(f"Successfully removed {removedNode}")
    # removedNode = ll.pop()
    # print(f"Successfully removed {removedNode}")

    # ll.printNode()
    # ll.prepend(1)
    # ll.printNode()
    # ll.popFirst()
    # ll.popFirst()
    # ll.popFirst()
    # ll.printNode()

    # getNode = int(input("Please enter the node index: "))
    # print(ll.get(getNode))
    # ll.popFirst()
    # getNode = int(input("Please enter the node index: "))
    # print(ll.get(getNode))
    ll.set_value(5,10000)
    ll.insert_value(6,100000000)
  
    ll.printNode()
    ll.remove_item(2)
    ll.printNode()