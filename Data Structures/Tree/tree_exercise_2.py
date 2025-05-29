class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None


    def add_child(self,child):
        child.parent = self
        self.children.append(child)


    def print_tree(self, level):
        if self.get_level()>level:
            return
        pad = ' '* 3 * self.get_level()
        prefix = pad + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)


    def get_level(self):
        level = 0
        p = self.parent
        
        while p:
            level+=1
            p = p.parent
        
        return level
    

def build_management_tree():

    state1 = TreeNode("Gujarat")
    state1.add_child(TreeNode("Ahmedabad"))
    state1.add_child(TreeNode("Baroda"))

    state2 = TreeNode("Karnataka")
    state2.add_child(TreeNode("Bengaluru"))
    state2.add_child(TreeNode("Mysore"))


    state3 = TreeNode("New Jersey")
    state3.add_child(TreeNode("Princeton"))
    state3.add_child(TreeNode("Trenton"))

    state4 = TreeNode("California")
    state4.add_child(TreeNode("San Francisco"))
    state4.add_child(TreeNode("Mountain View"))
    state4.add_child(TreeNode("Palo Alto"))

    country1 = TreeNode("India")
    country1.add_child(state1)
    country1.add_child(state2)

    country2 = TreeNode("USA")
    country2.add_child(state3)
    country2.add_child(state4)

    glob = TreeNode("Global")
    glob.add_child(country1)
    glob.add_child(country2)



    return glob


if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree(0)