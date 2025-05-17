class Node:
    def __init__(self, data=None, next =None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print("Empty Linked List")
            return
        
        itr = self.head
        listr = ''
        while itr:
            listr+= str(itr.data) + '->'
            itr = itr.next
        print(listr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr=itr.next
        itr.next = Node(data, None)

    def insert_values (self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


    def get_len(self):
        countr =0
        itr=self.head
        while itr:
            countr+=1
            itr = itr.next

        return countr
        
    def remove(self,index):

        if index<0 or index>=self.get_len():
            raise Exception("Invalid Index")
        
        if index==0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next= itr.next.next
                break

            itr = itr.next
            count+=1

    def insert(self,index,val):

        if index<0 or index>=self.get_len():
            raise Exception("Invalid Index")
        
        if index==0:
            self.insert_at_beginning(val)
            return

        count =0
        itr=self.head
        while itr:
            if count==index-1:
                node = Node(val, itr.next)
                itr.next = node
                break
            itr = itr.next
            count = count+1

    def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list

        if self.head is None:
            raise ("Blank Linked List")
        
        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return
        
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_after,itr.next)
                break
            itr = itr.next
            index +=1
        


    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head is None:
            raise ("Blank Linked List")
        
        if self.head.data==data:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next  


if __name__=="__main__":
    ll = LinkedList()
    ll.insert_values(['ab','red','99',21.4])
    ll.print()
    # ll.remove(2)
    # ll.print()
    # ll.remove(20)
    # ll.insert(0,"blue")
    # ll.print()
    # ll.insert(2,"blue")
    # ll.print()
    # ll.insert_after_value('red',15)
    # ll.print()
    ll.remove_by_value('red')
    ll.print()