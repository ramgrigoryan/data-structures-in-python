class Stack():
    def __init__(self):
        self.data = []
    
    def push(self,value):
        self.data.append(value)
    
    def pop(self):
        if self.data:
            self.data.pop()

    def peek(self):
        return self.data[len(self.data)-1]

    def isEmpty(self):
        return bool(not len(self.data))

my_stack = Stack()

my_stack.push(4)
my_stack.push(8)
my_stack.push(12)

print(my_stack.__dict__)

my_stack.pop()
my_stack.pop()

print(my_stack.isEmpty())

print(my_stack.__dict__)

        