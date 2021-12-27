def bubble_sort(elements, key):

    what = key
    for k in range(len(elements)-1):
        swapped = False
        for i in range(len(elements) - 1 - k):

            if elements[i][what] > elements[i + 1][what]:
                tmp = elements[i]
                elements[i] = elements[i + 1]
                elements[i + 1] = tmp
                swapped = True

        if not swapped:
            break


if __name__ == '__main__':

    element = [
        {'name': 'mona', 'trans_amount': 9, 'device': 'vivo'},
        {'name': 'dhaval', 'trans_amount': 90, 'device': 'google_pixel'},
        {'name': 'kathy', 'trans_amount': 1, 'device': 'vivo'},
        {'name': 'aamir', 'trans_amount': 4, 'device': 'ivo'},

     ]
    bubble_sort(element, key='name')
    print(element)
