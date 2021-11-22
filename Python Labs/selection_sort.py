# TODO: Write a selection_sort_descend_trace() function that 
#       sorts the numbers list into descending order
import doctest
def selection_sort_descend_trace(numbers):
    """Function that sorts a list in descending order using
    selection sort.
    >>> selection_sort_descend_trace([20, 10, 30, 40])
    40 10 30 20 
    40 30 10 20 
    40 30 20 10 
    >>> selection_sort_descend_trace([90, 95, 20, 1, 30, 55, 4])
    95 90 20 1 30 55 4 
    95 90 20 1 30 55 4 
    95 90 55 1 30 20 4 
    95 90 55 30 1 20 4 
    95 90 55 30 20 1 4 
    95 90 55 30 20 4 1 
    >>> selection_sort_descend_trace([])
    >>> selection_sort_descend_trace([20, 20, 20, 20])
    20 20 20 20 
    20 20 20 20 
    20 20 20 20 
    >>> selection_sort_descend_trace([-5, -10, 30, -40, 5])
    30 -10 -5 -40 5 
    30 5 -5 -40 -10 
    30 5 -5 -40 -10 
    30 5 -5 -10 -40 
    """
    for selection_index in range(len(numbers) - 1):
        max_value_found = numbers[selection_index]
        max_value_index = selection_index
        for compare_index in range(selection_index + 1, len(numbers)):
            if numbers[compare_index] > max_value_found:
               max_value_found = numbers[compare_index]
               max_value_index = compare_index
        temp_value = numbers[selection_index]
        numbers[selection_index] = max_value_found
        numbers[max_value_index] = temp_value
        str_to_print = ""
        for index in range(len(numbers)):
            str_to_print += str(numbers[index]) + " "
        print(str_to_print)


if __name__ == "__main__":
    # TODO: Read in a list of integers into numbers, then call
    #       selection_sort_descend_trace() to sort the numbers
    doctest.testmod()
    user_numbers = input().split()
    user_numbers = [int(num) for num in user_numbers]
    selection_sort_descend_trace(user_numbers)