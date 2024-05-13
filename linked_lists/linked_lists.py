class Linked_List():
    def __init__(self,value):
        self.head = {
            "value":value,
            "next":None
        }
        self.tail = self.head
        self.length = 1
    
    def prepend(self,value):
        new_node = {"value":value,"next":self.head}
        self.head = new_node
        self.length +=1

    def append(self,value):
        new_tail = {
            "value":value,
            "next":None
        }
        self.tail["next"]=new_tail
        self.tail = new_tail
        self.length += 1

    def instert(self,index,value):
        i = 0
        prev_node = self.head
        if (i==index):
            new_node = {"value":value,"next":self.head}
            self.head = new_node
            self.length +=1 
            return
        while i!=index-1:
            prev_node= prev_node["next"]
            i +=1
        if(i==index-1):
            new_node = {"value":value,"next":prev_node["next"]}
            prev_node["next"] = new_node
            if new_node["next"] == None:
                self.tail = new_node
            self.length+=1
    
    def remove(self,index):
        i=0
        prev_node = None
        current_node = self.head
        while i != index:
            prev_node = current_node
            current_node = current_node["next"]
            i +=1
        if current_node == self.head:
            self.head = current_node["next"]
            self.length -=1
            return
        if current_node== self.tail:
            self.tail = prev_node
            prev_node["next"] = None
            self.length -=1
            return
        prev_node["next"] = current_node["next"]
        self.length -=1
        
        
        
    
    def traverse(self):
        all_nodes = []
        current_node = self.head
        if self.head == self.tail:
            all_nodes.append(current_node)
            return all_nodes
        while current_node["next"] != None:
            all_nodes.append((current_node))
            current_node = current_node["next"]
        all_nodes.append(current_node)
        
        return all_nodes

my_linked_list = Linked_List(10)

my_linked_list.append(6)

my_linked_list.append(16)

my_linked_list.prepend(8)

my_linked_list.instert(0,4)

my_linked_list.instert(2,2)
my_linked_list.instert(6,19)
my_linked_list.instert(6,29)

my_linked_list.remove(0)

my_linked_list.remove(2)

print(my_linked_list.head)
