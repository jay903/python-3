class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_children(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = '  ' * self.get_level()*3
        prefix=spaces + "|__" if self.parent else ""

        print(prefix + self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_children(TreeNode("mac")) # Treenode data here is pass as a argument to a add_children method
    laptop.add_children(TreeNode("Surface"))
    laptop.add_children(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_children(TreeNode("Iphone"))
    cellphone.add_children(TreeNode("Samsung"))
    cellphone.add_children(TreeNode("Vivo"))

    root.add_children(laptop)
    root.add_children(cellphone)

    return root

if __name__ == "__main__":
    root=build_product_tree()

    root.print_tree()
    pass


