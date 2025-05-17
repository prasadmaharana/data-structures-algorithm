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
        self.arr[h].append((key,val))

    
    def __getitem__(self,index):
        h = self.get_hash(index)
        for element in self.arr[h]:
            if element[0] == index:
                return element[1]
        raise KeyError(f'Key {index} not found')
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
                return
        raise KeyError(f'Key {key} not found')


if __name__=='__main__':
    t = HashTable()
    t["march 6"] = 310
    t["march 7"] = 420
    t["march 8"] = 67
    t["march 17"] = 63457
    t["march 25"] = 18
    print(t.arr)

