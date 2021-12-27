a=['10','20','70','90']
print(len(a)+1)
for j in range(len(a)-1):
    a[j]=a[j+1]
    j+=1
    if j==(len(a)-1):
        a.pop(j)
       
print(a)