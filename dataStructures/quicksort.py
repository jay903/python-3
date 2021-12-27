'''
Hoare partition
start and end and the element is swapped with the end element

'''


def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start<len(elements) and elements[start] <= pivot:  # start is less than len elements and elements of start is less than pivot
            start += 1

        while elements[end] > pivot: #till end is greater than pivot minus end
            end -= 1

        if start < end:  # indexes are compared when start crosses end  swap start and end
            swap(start, end, elements) # swapping of start and end when element[start] > 11 and end element is less than 11

    swap(pivot_index, end, elements) #this swapping is done when end cross start ' swap end and pivot

    return end


def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1) #left partition
        quick_sort(elements, pi+1, end) #right partition


if __name__ == '__main__':
    #element=[11, 9, 29, 7, 2, 15, 28]
    tests=[
        [11,9,29,7,2,15,28],
        [3,7,9,11],
        [25,22,21,10],
        [29,15,28],
        [],
        [6]

    ]
    for element in tests:
        quick_sort(element, 0, len(element)-1)
        print(element)
