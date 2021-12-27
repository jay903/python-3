class Node:
    def __init__(self,data=None,Next=None):
        self.data=data
        self.Next=Next
        

class LinkedList:
    def __init__(self):
        self.head=None
    
    def inserAtBeginning(self,data):
        node=Node(data,self.head)
        self.head=node
        
    def print(self):
        if self.head is None:
            print("linked list is empty")
            
        itr=self.head
        llstr=''
        while itr:
            llstr += str(itr.data) + "------>"
            itr=itr.Next
        print(llstr)
        
        
    def insertAtEnd(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr=self.head
        while itr.Next:
            itr=itr.Next
            
        itr.Next=Node(data, None)
        
    def insertValues(self, data_list):
        self.head = None
        for data in data_list:
            self.insertAtEnd(data)

    def removeAt(self,index):
        if index < 0 and index > self.get_length():
            raise Exception("invalid index")
        
        if index == 0:
            self.head = self.head.Next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.Next = itr.Next.Next
                break
            itr = itr.Next
            count += 1
            
    def insertAt(self, index, data):
        if index<0 and index>self.get_length():
            raise Exception("invalid index")
        
        if index==0:
            self.inserAtBeginning(data)
            return
        itr=self.head
        count=0
        while itr:
            if count==index-1:
                node=Node(data,itr.Next)
                itr.Next=node
                break
            itr=itr.Next
            count += 1
            
if __name__=='__main__':
    ll=LinkedList()
    ll.inserAtBeginning(12)
    ll.inserAtBeginning(34)
    ll.inserAtBeginning(90)
    ll.insertAt(10, 1234)
    ll.insertAtEnd(56)
    ll.removeAt(10)
    ll.print()