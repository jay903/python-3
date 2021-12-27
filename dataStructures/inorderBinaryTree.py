# in order traversal main node is traverse in between
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:    # checks if value already exist don't need to add anything
            return
        if data < self.data:
            if self.left:   # checks if value already their in left side if not present else part is executed
                self.left.add_child(data)  # recursion self.left is just another subtree
            else:       # self.left is assigned here
                self.left = (BinaryTree(data))
        else:  # same thing as above with right tree
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinaryTree(data)

    def in_order_traversal(self):
        elements=[]
        # visit left
        if self.left:
            elements += self.left.in_order_traversal()
        # visit base
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def search(self , val):

        if self.data == val:
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

        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):

        if self.right is None:
            return self.data     # return the last elements which is always highest
        return self.right.find_max()

    def delete(self,val):
        if val < self.data:  # if lesss than current node go left
            if self.left:
                self.left=self.left.delete(val)

        elif val > self.data:
            if self.right:
                self.right=self.right.delete(val) # after deleting assign a new sub tree
        else:
            if self.left is None and self.right is None: # last data point return none with no right and left
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.left.find_min()  # so there are two methods to delete the item either assign the max value from the left node
                                            # or min value from the right sub node of a respective deleted node
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self




def build_tree (elements) :
    root=BinaryTree(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root
if __name__=="__main__":
    numbers=[17,4,1,20,9,23,18,34]
    numbers_tree=build_tree(numbers)
    numbers_tree.delete(34)
    print("after deleting ", numbers_tree.in_order_traversal())