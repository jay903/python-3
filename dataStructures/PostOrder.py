class PostOrder:
    def __init__(self,data):
        self.data= data

        self.left=None
        self.right=None

    def add_child(self,data):

        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=PostOrder(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=PostOrder(data)

    def post_order_traversal(self):
        elements=[]

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

def build_tree(elements):  # helper function
    root= PostOrder(elements[0]) # here root is defined as elements of 0

    for i in range (1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers= [10, 2, 34, 5, 67, 23, 4]
    numbers_tree= build_tree(numbers)
    print(numbers_tree.post_order_traversal())

