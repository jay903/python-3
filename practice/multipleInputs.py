class j:
   def sum(self,lst):
        sum=0
        for i in lst:
            sum +=i
        return sum

    
    
    
# creating an empty list
lst = []  
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
 
    lst.append(ele) # adding the element
     
j1=j()
print(f" the sum is  {j1.sum(lst)}")