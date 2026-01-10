from utils import time_it

@time_it
def linear_search(numbers_list, number_to_find):
    for index, number in enumerate(numbers_list):
        if number == number_to_find:
            return index

@time_it
def binary_search(numbers_list, number_to_find):

    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0


    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        middle_value = numbers_list[mid_index]

        if middle_value == number_to_find:
            return mid_index

        if number_to_find < middle_value:
            right_index = mid_index - 1
        else:
            left_index = mid_index + 1
    return -1


def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if left_index > right_index:
        return -1
    mid_index = (left_index + right_index) // 2

    middle_value = numbers_list[mid_index]

    if middle_value == number_to_find:

        return mid_index

    if number_to_find < middle_value:
        right_index = mid_index - 1
    else:
        left_index = mid_index + 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)





if __name__ == "__main__":
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 61]
    number_to_find = 61

    index = linear_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using linear search")


    binary_index = binary_search(numbers_list, number_to_find)
    print(f"Number found at index {binary_index} using binary search")

    binary_recursive_index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list) - 1)
    print(f"Number found at index {binary_recursive_index} using binary search recursive")