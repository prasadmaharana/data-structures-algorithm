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
    



def IsMatch(left_char, right_char):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'    
    }
    return match_dict[left_char] == right_char




def reverse_string(string):
    s =Stack()

    for i in string:
        s.push(i)

    rstr=''

    while s.size()!=0:
        rstr+=s.pop()

    return rstr


def IsBalanced(string):

    stack = Stack()

    for char in string:
        if char in ('(','{','['):
            stack.push(char)

        if char in (')','}',']'):
            if stack.size()==0:
                return False
            if stack.size()==0:
                return False
            if not IsMatch(char,stack.pop()):
                return False
            
    return stack.size()==0
        

if __name__== "__main__":
    st = Stack()
    string ="We will conquere COVID-19"
    print(reverse_string(string))
    print(IsBalanced("({a+b})"))
    print(IsBalanced("))((a+b}{"))
    print(IsBalanced("((a+b))"))
    print(IsBalanced("((a+g))"))
    print(IsBalanced("))"))
    print(IsBalanced("[a+b]*(x+2y)*{gg+kk}"))


