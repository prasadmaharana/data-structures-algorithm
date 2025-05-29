class TreeNode:
    def __init__(self,name, designation):
        self.name = name
        self.designation =designation
        self.children = []
        self.parent = None


    def add_child(self,child):
        child.parent = self
        self.children.append(child)


    def print_tree(self,type):
        
        if type=='both':
            value =  self.name + " (" + self.designation + ")"

        elif type == 'designation':
            value = self.designation
        
        else:
            value = self.name

        pad = ' '* 3 * self.get_level()
        prefix = pad + "|__" if self.parent else ""

        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(type)


    def get_level(self):
        level = 0
        p = self.parent
        
        while p:
            level+=1
            p = p.parent
        
        return level
    

def build_management_tree():
   
    level_cxo1= TreeNode('Chinmay', 'CTO')
    level_head1 = TreeNode('Vishwa','Infrastructure Head')
    level_head1.add_child(TreeNode('Dhaval','Cloud Manager'))
    level_head1.add_child(TreeNode('Abhijit','App Manager'))
    level_head2 = TreeNode('Aamir','Application Head')
    level_cxo1.add_child(level_head1)
    level_cxo1.add_child(level_head2)


    level_cxo2= TreeNode('Gels', 'HR Head')
    level_cxo2.add_child(TreeNode('Peter','Recruitment Manager'))
    level_cxo2.add_child(TreeNode('Waqas','Policy Manager'))

    ceo= TreeNode('Nilupul', 'CEO')
    ceo.add_child(level_cxo1)
    ceo.add_child(level_cxo2)

    return ceo


if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy