s="my name is jay sawant , i live in ashvem mandrem pernem goa and my home address is also same , \nthank you for hearing me and , thanks once again"
"""print(s.split(','))
j='jay'
print(j.isalpha())
print(s.replace('jay','harish'))
print(s.upper())
print(s.rstrip())"""

list=['jay',12,'wer',True]
"""print(list[1:-1])
print((list.append(12)))
print(list.pop(2))
print(list)
"""

M = ['bb', 'aa', 'cc']
"""M.sort()
print(M)
M.reverse()
print(M)"""

k=[
    [12,45,56],
    [4, 5,  6],
    [89,78,98]
]

"""diag=[k[i][i] for i in [0,1,2]] #this gives diagonal
print(diag)"""
"""p=[2,6,8]
list(map(sum,p))"""


"""sum=0"""
"""for i in k[:]: #here i contains list      this loop gives sum of each column
    sum = 0
    for j in i:
      sum+=j
    print(sum)"""

"""print(k[0][2]) #56
print(k[2][2]) #98
print(k[1]) #4 5 6
col2=[row[1] for row in k] #gives the column 1#==============================================imp============================
print(col2) #45 5 78
colMod=[row[1] for row in k if row[1]% 2==0] #============================================imp================================
print(colMod) #78"""

lis=['a','b','v']
s="-"
s=s.join(lis)
print(s)