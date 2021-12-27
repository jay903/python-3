class PreOrder:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:  # if
            if self.left:
                self.left.add_child(data)
            else:
                self.left = (PreOrder(data))
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = PreOrder(data)

    def pre_order_traversal(self):
        elements= []

        elements.append(self.data)  # visits the base node first

        if self.left:
            elements += self.left.pre_order_traversal() # visits the left node

        if self.right:
            elements += self.right.pre_order_traversal()
        return elements


def build_tree(elements):
    root = PreOrder(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == "__main__":
    numbers = [40, 30, 35, 20, 80, 100]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.pre_order_traversal())