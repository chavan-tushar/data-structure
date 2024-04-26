class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
class Queue:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.bottom = new_node
        self.height = 1
    
    def print_queue(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next
        
    def enque(self,value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            temp = self.bottom
            temp.next = new_node
            self.bottom = new_node
        self.height += 1
        return True

    def dequeue(self):
        if self.height == 0:
            return None
        temp = self.top
        if self.height == 1:
            self.top = self.bottom = None
        else:
            self.top = temp.next
            temp.next = None
        self.height -= 1

        return temp
        

if __name__ == "__main__":
    q1 = Queue(1)
    q1.enque(2)
    q1.enque(3)
    q1.print_queue()
    removed = q1.dequeue()
    print(f"Successfully Removed {removed.value}" if removed else "No elements in Queue to remove.")
    removed = q1.dequeue()
    print(f"Successfully Removed {removed.value}" if removed else "No elements in Queue to remove.")
    removed = q1.dequeue()
    print(f"Successfully Removed {removed.value}" if removed else "No elements in Queue to remove.")
    removed = q1.dequeue()
    print(f"Successfully Removed {removed.value}" if removed else "No elements in Queue to remove.")
    q1.print_queue()
    q1.enque(10)
    q1.enque(20)
    q1.print_queue()