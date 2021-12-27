
class dict:
    def __init__(self,name):
        self.name=name
    def val(self,dict0):
        for key in dict0:
            print("key:",key,"=> value----->",dict0[key])
            print(self.name)

    def listed(self,list1):
        print("\n")
        for val in list1:
            
            print(f"{self.name}   {val}-------------------->times be good")
           
        
jay={
    1:"happy",
    2:"famous",
    3:"average",
    4:"cold"
}

hary=[10,23,56,90]
d=dict("jay")
d.val(jay)
d.listed(hary)