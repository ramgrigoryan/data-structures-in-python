class HashTable():
    def __init__(self):
        self.data = [None] *50
    
    def _hash(self,key):
        hash = 0
        for i in range(0,len(key)):
            hash = (hash + ord(key[i])*(i+1))%len(self.data)
        return hash
    
    def set(self,key,value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append((key,value))
        return self.data

    def get(self,key):
        address = self._hash(key)
        for element in self.data[address]:
            if element[0] == key:
                return element[1]
        return None
    
    def keys(self): # O(n)-best case, O(n^2)-worst case (collision) 
        all_keys = []
        for elements in self.data:
            if elements:
                for item in elements:
                    all_keys.append(item[0])
        return all_keys
    
my_object = HashTable()

my_object.set("Vahram","is amazing")

vahram = my_object.get("Vahram")

my_object.set("Ani","Is beautiful!")

ani = my_object.get("Ani")

my_object.set("ani","Is funny!")

ani2 = my_object.get("ani")

# print(vahram,ani,ani2)

print(my_object.keys())