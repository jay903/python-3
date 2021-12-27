l1=[1,4,6]
l2=[8,2,7]
def mergeTwoList(l1,l2):
    if not l1 or not l2:
        return l1 or l2

    if l1.val < l2.val:
        l1.next=mergeTwoList(l1.next,l2)
        return l1
    else:
        l2.next=mergeTwoList(l1,l2.next)
        return l2

print(mergeTwoList(l1,l2))