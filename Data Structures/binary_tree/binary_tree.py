class BinarySearchTreeNode:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data==self.data:
            return

        if data < self.data:
            #add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            #add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def find_min(self):

        if self.left:
            return self.left.find_min()
        return self.data


    def find_max(self):

        if self.right:
            return self.right.find_max()
        return self.data    
    

    def InorderTraversal(self):
        elements=[]
        #visit left tree
        if self.left:
            elements+=self.left.InorderTraversal()
        #visit node
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements+=self.right.InorderTraversal()

        return elements
    

    def search(self,val):

        if self.data==val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)

            else:
                return False
        
        if val > self.data:
            if self.right:
                return self.right.search(val)

            else:
                return False

    def delete(self,val):

        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)

        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        else:

            if self.left is None and self.right is None:
                return None

            if self.left is None:
                return self.right
            
            if self.right is None:
                return self.left
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self
        


def buildtree(elements):

    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


if __name__=='__main__':

    numbers = [17,4,1,20,9,15,18,22,18]
    tree = buildtree(numbers)
    print(tree.InorderTraversal())
    print(tree.search(18))