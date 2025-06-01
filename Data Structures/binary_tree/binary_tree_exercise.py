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
    
    def PreOrderTraversal(self):
        elements=[]

        #visit node
        elements.append(self.data)

        #visit left tree
        if self.left:
            elements+=self.left.PreOrderTraversal()

        #visit right tree
        if self.right:
            elements+=self.right.PreOrderTraversal()

        return elements
         

    def PostOrderTraversal(self):
        elements=[]

        #visit left tree
        if self.left:
            elements+=self.left.PostOrderTraversal()

        #visit right tree
        if self.right:
            elements+=self.right.PostOrderTraversal()

        #visit node
        elements.append(self.data)    

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
            


    def find_min(self):

        if self.left:
            return self.left.find_min()
        return self.data



    def find_max(self):

        if self.right:
            return self.right.find_max()
        return self.data
    

    def calculateSum(self):
        left= self.left.calculate_sum() if self.left else 0
        right = self.right.calculate_sum() if self.right else 0
        return self.data + left + right



def buildtree(elements):

    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root




if __name__=='__main__':

    numbers = [15,12,27,7,14,20,23,88]
    tree = buildtree(numbers)
    print(tree.find_min())
    print(tree.find_max())