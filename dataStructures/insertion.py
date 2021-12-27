
def insertion_sort(element):
    for i in range(1,len(element)):
        anchor=element[i]
        j=i-1
        while j>=0 and anchor<element[j]:
            element[j+1]=element[j]
            j=j-1
        element[j+1]=anchor


if __name__ == '__main__':
    elements = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    insertion_sort(elements)
    print(elements)