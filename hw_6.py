def bubble_sort(list_):
    for n in range(len(list_)):
        swapped = False
        for index in range(len(list_) - 1 - n):
            if list_[index] > list_[index + 1]:
                list_[index], list_[index + 1] = list_[index + 1], list_[index]
                swapped = True
        if not swapped:
            break
list_ = [12, 64,100,55,10,111,666,345,1,0,354]
print(f'Unsorted list is: {list_}')

bubble_sort(list_)

print(f'Sorted list is: {list_}')

def binary_search(value,N = 5000):
    array = list(range(N))
    First = 0
    ResultOk = False
    Last = len(array) - 1
    pos = -1

    while First <= Last:
        Middle = (First + Last) // 2
        if array[Middle] == value:
            ResultOk = True
            pos = Middle
            break
        elif array[Middle] < value:
            First = Middle + 1
        else:
            Last = Middle - 1

    if ResultOk:
        print(f'Элемент {value} найден на позиции: {pos}')
        return pos
    else:
        print(f'Элемент {value} не найден')
        return -1

value_to_find = 1
binary_search(value_to_find)


