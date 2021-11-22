import os
import doctest

CURRENT_FILE_PATH = os.getcwd()

def get_items_from_dir(file_path):
    total_items_in_dir = []

    first_iteration = False
    for dir_names, sub_names, file_names in os.walk(file_path):
        if not first_iteration:
            first_iteration = True
            for file in file_names:
                total_items_in_dir.append(file)
        else:
            dir_name = os.path.basename(dir_names)
            dir_name = (dir_name + "/")
            total_items_in_dir.append(dir_name)

    total_items_in_dir.sort()

    return total_items_in_dir

def print_list(list):
    """Prints all elements of a list
    >>> print_list([1, 2, 3, 4, 5, 6])
    1
    2
    3
    4
    5
    6
    >>> print_list([])
    """
    for item in list:
        print(item)

item_list = get_items_from_dir(CURRENT_FILE_PATH)
print_list(item_list)

if __name__ == '__main__':
    doctest.testmod()