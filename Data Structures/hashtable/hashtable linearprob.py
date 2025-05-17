class HashTable:
    def __init__(self):
        self.MAX= 10
        self.arr = [[] for _ in range (self.MAX)]

    def get_hash(self, key):
        h=0
        for char in key:
            h+=ord(char)
        return h % self.MAX
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h].append((key,val))
        else:
            new_h = self.find_loc(key, h)
            self.arr[new_h].append((key,val))
        print(self.arr)


    def find_loc(self, key, index): 
        slots = self.get_range(index)

        for slot in slots:
            if self.arr[slot] is None:
                return slot
            if self.arr[slot][0]== key:
                return slot
        raise Exception("Hash Map Full") 

    
    def __getitem__(self,key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        slots = self.get_range(key)

        for slot in slots:
            element = self.arr[slot]

            if element is None:
                return
            if element[0]== key:
                return element[1]
    
    def __delitem__(self, key):
        h = self.get_hash(key)

        if self.arr[key] is None:
            return

        slots = self.get_range(key)

        for slot in slots:
            element = self.arr[slot]

            if element is None:
                raise Exception ("Key does not exist")
            if element[0]==key:
                element[0] = None
            

    def get_range(self, index):
        return [*range(index, len(self.arr)) + [*range(0, index)]]



if __name__=='__main__':
    t = HashTable()
    t["march 6"] = 310
    t["march 7"] = 420
    t["march 8"] = 67
    t["march 17"] = 63457
    t["march 25"] = 18
    print(t.arr)

