def bubble_sort(elemnents):
    size=len(elements)

    for k in range(size-1):
        swapped = False
        for i in range(size-1-k):
            if elemnents[i] > elemnents[i+1]:
                tmp = elemnents[i]
                elemnents[i] = elemnents[i+1]
                elements[i+1] = tmp
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    elements = [5, 9, 2, 1, 67, 34, 88, 34]
    bubble_sort(elements)
    print(elements)