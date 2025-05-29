class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children =[]
        self.parent = None


    def add_child(self,child):
        child.parent = self
        self.children.append(child)


    def print_tree(self):
        pad = ' '* 3 * self.get_level()
        prefix = pad + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


    def get_level(self):
        level = 0
        p = self.parent
        
        while p:
            level+=1
            p = p.parent
        
        return level


def build_product_tree():
    root= TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Macbook"))
    laptop.add_child(TreeNode("Thinkpad"))
    laptop.add_child(TreeNode("Surface"))


    mobile = TreeNode("Mobiles")
    mobile.add_child(TreeNode("iPhone"))
    mobile.add_child(TreeNode("Google Pixel"))
    mobile.add_child(TreeNode("Vivo"))


    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Sony"))

    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(tv)

    return root


if __name__ =='__main__':
    root = build_product_tree()
    root.print_tree()