class Node:
    def __init__(self, data=None, next =None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        if self.head ==None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr
    
    def print_forward(self):
        if self.head is None:
            print("Empty Linked List")
            return
        
        itr = self.head
        listr = ''
        while itr:
            listr+= str(itr.data) + '->'
            itr = itr.next
        print(listr)

    def print_backward(self):
        if self.head is None:
            print("Empty Linked List")
            return
        
        last_node = self.get_last_node()
        itr = last_node
        listr = ''
        while itr:
            listr+= str(itr.data) + '->'
            itr = itr.prev
        print(listr)    


    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        
        itr = self.head
        while itr.next:
            itr=itr.next
        itr.next = Node(data, None, itr)


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
            self.head.prev = None
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next= itr.next.next

                if itr.next:
                    itr.next.prev = itr
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
                node = Node(val, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count = count+1

    def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list

        if self.head is None:
            raise ("Blank Linked List")
        
        itr = self.head
        while itr:
            if itr.data == data_after:
                new_node = Node(data_to_insert,itr.next, itr)

            if itr.next:
                itr.next.prev = new_node
                break

            itr = itr.next
        


    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head is None:
            raise ("Blank Linked List")

        itr = self.head
        while itr:
            if itr.data == data:
                if itr.prev is None:
                    self.head = itr.next
                    if self.head:
                        self.head.prev = None
                else:
                    itr.prev.next = itr.next
                    if itr.next:
                        itr.next.prev = itr.prev

            itr = itr.next  


if __name__=="__main__":
    ll = DoubleLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert(0,"jackfruit")
    ll.print_forward()
    ll.insert(5,"dates")
    ll.print_forward()
    ll.insert(2,"kiwi")
    ll.print_forward()
    ll.remove_by_value('kiwi')
    ll.print_forward()