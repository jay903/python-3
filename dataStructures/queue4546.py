from collections import deque

class queue:
    def __init__(self):
        self.collection=deque()
        
    def queueAppend(self,data):
        self.collection.append(data)
    
    def pop(self):
        self.collection.popleft()
    def print(self):
        print(self.collection)


q=queue()
q.queueAppend(30)
q.queueAppend(40)
q.queueAppend(67)
q.print()
q.pop()
q.print()
'''queue=deque()

queue.append(40)
queue.append(34)
queue.append(90)
print(queue)
queue.popleft()
print(queue)'''






