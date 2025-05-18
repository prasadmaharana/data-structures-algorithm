from collections import deque

class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def IsEmpty(self):
        return len(self.buffer)==0
    
    def size (self):
        return len(self.buffer)
    
    def EnqueueDict(self, key, value):
        self.buffer.appendleft({key: value})
    


if __name__=="__main__":
    data = Queue()

    data.enqueue({
        'companyname':'Apple', 
        'timestamp':'18 May 2025, 11:02 AM', 
        'price':'211.11' 
    })
    data.enqueue({
        'companyname':'Apple', 
        'timestamp':'18 May 2025, 11:03 AM', 
        'price':'211.21' 
    })
    data.enqueue({
        'companyname':'Apple', 
        'timestamp':'18 May 2025, 11:04 AM', 
        'price':'211.56' 
    })
    data.enqueue({
        'companyname':'Apple', 
        'timestamp':'18 May 2025, 11:05 AM', 
        'price':'211.78' 
    })

    data.enqueue({
        'companyname':'Apple', 
        'timestamp':'18 May 2025, 11:06 AM', 
        'price':'212.11' 
    })

    for i in range (0,3):
       print(data.dequeue())




