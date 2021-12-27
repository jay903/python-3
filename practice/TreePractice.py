class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_children(self,child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        level=0
        p=self.parent
        while p:
            level += 1

            p =p.parent

        return level

    def print_tree(self):
        spaces = '  ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""

        print(prefix + self.data)
        if len(self.children)>0:
            for child in self.children:
             child.print_tree()

def build_company_tree():
    root=TreeNode("Nilupul (CEO)")

    chinmay=TreeNode("Chinmay (CTO")
    chinmay.add_children(TreeNode("Aamir (Application Head)"))
    vishva=TreeNode("vishva (Infrastructural Head)")
    vishva.add_children(TreeNode("Dhval (Cloud Manager)"))
    vishva.add_children(TreeNode("Abhijit (App Manager"))

    root.add_children(chinmay)
    chinmay.add_children(vishva)
    Gels=TreeNode("Gels (HR Head)")
    root.add_children(Gels)
    Gels.add_children(TreeNode("Peter (Recruitment Manager)"))
    Gels.add_children(TreeNode("waqas (Policy Manager"))



    return root
if __name__ == "__main__":
    root=build_company_tree()

    root.print_tree()
