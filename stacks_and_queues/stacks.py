class Node():
    def __init__(self,value=None,next=None):
        self.value = value 
        self.next = next

class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self,value):
        next = self.top
        new_node = Node(value=value,next=next).__dict__
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        self.top = new_node
        self.length +=1

    def pop(self):
        if self.top:
            self.top= self.top["next"]
            if self.top == None:
                self.bottom = None
            self.length -=1

    def peek(self):
        return self.top['value']

    def isEmpty(self):
        return bool(not self.length)

my_stack = Stack()

my_stack.push(5)
my_stack.push(10)
my_stack.push("Hello, world")

print(my_stack.peek())

print(my_stack.__dict__,my_stack.length)

my_stack.pop()
my_stack.pop()

print(my_stack.__dict__,my_stack.length)

print(my_stack.isEmpty())

