num_cals = 0

def partition(list, first_index, last_index):
    """Helper function for quicksort function. Determines the pivot point of a list and moves
    the other values from one side to the other according to the value of the pivot point.
    >>> user_list = [6, 2, 4, 7]
    >>> partition(user_list, 0, 3)
    0
    >>> str(user_list)
    '[2, 6, 4, 7]'
    >>> partition([6, 2, 4, 7], 2, 3)
    2
    >>> str(user_list)
    '[2, 6, 4, 7]'
    >>> user_list = []
    >>> partition(user_list, 0, 0)
    """
    if len(list) > 0:
        middle_index = (first_index + last_index) // 2
        pivot_item = list[middle_index]

        left_index = first_index
        right_index = last_index

        while True:
            while list[left_index] < pivot_item:
                left_index += 1
            while pivot_item < list[right_index]:
                right_index -= 1
            
            if left_index >= right_index:
                break
            else:
                temp_value = list[left_index]
                list[left_index] = list[right_index]
                list[right_index] = temp_value
                
                left_index += 1
                right_index -= 1
        
        middle_index = right_index
        return middle_index
        

def quicksort(list, begin_index, end_index):
    """Given a list and a initial index and end index, the function
    uses quicksort algorithm to sort its items. Increments the 
    global variable num_cals every time quicksort is called.
    >>> item_list = [7, 3, 8, 1]
    >>> quicksort(item_list, 0, 3)
    >>> str(item_list)
    '[1, 3, 7, 8]'
    >>> item_list = ['b', 'y', 'r', 'i', 'p']
    >>> quicksort(item_list, 0, 4)
    >>> str(item_list)
    "['b', 'i', 'p', 'r', 'y']"
    >>> item_list = []
    >>> quicksort(item_list, 0, 0)
    """
    if len(list) > 0:
        #print(list)
        global num_cals
        num_cals += 1
        if begin_index >= end_index:
            return
        else:
            middle_index = partition(list, begin_index, end_index)

            quicksort(list, begin_index, middle_index)
            quicksort(list, middle_index + 1, end_index)
            return

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    user_list = []
    while True:
        user_input = input()
        if user_input == '-1':
            break
        else:
            user_list.append(user_input)

    quicksort(user_list, 0, len(user_list) - 1)

    print(num_cals)
    for item in user_list:
        print(item)