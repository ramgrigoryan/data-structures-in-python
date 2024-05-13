
class MyArray():
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self,index):
        return self.data[index]
    
    def append(self,value):
        self.data[self.length] = value
        self.length +=1

    def insert(self, position, value):
        if position<self.length and position>=0:
            for i in range(self.length-1,position-1,-1):
                self.data[i+1]= self.data[i]
            self.data[position] = value
            self.length +=1
        elif position == self.length:
            self.data[position] = value
            self.length +=1
        else:
            print("Error")
    
    def pop(self,position):
        if (position>=self.length or position<0):
            print("Error")
            return
        elif position== self.length -1:
            self.data.pop(position)
            self.length -= 1
        else:
            for i in range(position,self.length-1):
                self.data[i] = self.data[i+1]
            self.data.pop(self.length-1)
            self.length -=1