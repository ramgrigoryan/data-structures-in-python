class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def enqueue(self,value):
        
        new_node = Node(value)
        
        if not self.first:
            self.first= new_node
            self.last = new_node
            self.length+=1
            return
        
        self.last.next = new_node
        self.last = new_node
        self.length+=1
    
    def dequeue(self):
        if self.first:
            self.first = self.first.next
            self.length -=1

    def peek(self):
        return self.first.value

    def isEmpty(self):
        return bool(not self.length)

    def traverse(self):
        data = []
        current_node = self.first
        while current_node:
            data.append(current_node.value)
            current_node = current_node.next
        return data

my_queue = Queue()

my_queue.enqueue("Vahram")

my_queue.enqueue("Srbuhi")

my_queue.enqueue("Miley")



print(my_queue.traverse())

my_queue.dequeue()

print(my_queue.peek())

my_queue.dequeue()
print(my_queue.traverse())