from collections import deque 

class Stack:

    def __init__(self):
        self.container = deque()
        
    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]
    
    def IsEmpty (self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    

if __name__== "__main__":
    st = Stack()
    st.push(5)
    st.push(21)
    st.push(222)
    st.push(81)
    st.push(9981)
    print(st.container)
