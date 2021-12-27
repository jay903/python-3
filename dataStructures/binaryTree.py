def linear_search(number_list, numbers_to_find):
    for i , element in enumerate(number_list):
        if element==numbers_to_find:
            return i
    return -1


def binary_search(number_list,number_to_find):
    left_index = 0
    right_index = len(number_list)-1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index+right_index)//2

        mid_number=number_list[mid_index]
        count=0
        if mid_number== number_to_find:
            count +=1
            return count

        if mid_number<number_to_find:
            left_index=mid_index+1
        else:
            right_index=mid_index-1
    return -1


def binary_search_recursive(number_list,number_to_find,left_index,right_index):
    if right_index < left_index:
        return -1
    mid_index =(left_index + right_index)//2
    mid_number=number_list[mid_index]

    if mid_number==number_to_find:
        return mid_index
    if mid_number < number_to_find:
        left_index=mid_index+1
    else:
        right_index=mid_index-1

    return binary_search_recursive(number_list,number_to_find,left_index,right_index)

def how_many_times(number_list,number_to_find):
        count=0
        for i in number_list:
            if i==number_to_find:
                count +=1
        return count





if __name__ == '__main__':
    numbers_list=[1,3,4,67,90,990]

    number_to_find=67

    """index = linear_search(numbers_list,number_to_find)
    print(f"number found at index {index} using linear serach")"""

    bindex=binary_search_recursive(numbers_list,number_to_find,0,len(numbers_list)-1)
    print(f"number found at index {bindex} using binary serach")
    c=how_many_times(numbers_list,number_to_find)
    print(f"number 67 is {c}")