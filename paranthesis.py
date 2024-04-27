class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
    
class Stack:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self,value):
        new_node = Node(value)
        temp = self.top
        self.top = new_node
        if self.height > 0:
            self.top.next = temp
        
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = temp.next
            temp.next = None
        self.height -= 1

if __name__ == "__main__":
    def checkParanthesis(str):
        if len(str) == 0:
            return True
        s1 = Stack(str[0])
        for char in str[1:]:
            if s1.height == 0 and char == ")":
                return False
            elif char == "(":
                s1.push("(")
            else:
                s1.pop()
        if s1.height > 0:
            return False
        else:
            return True

    str = ""
    print(checkParanthesis(str))    
    

