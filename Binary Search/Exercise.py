from utils import time_it

@time_it
def find_occurrences(numbers, number_to_find):
    left_index = 0
    right_index = len(numbers) - 1
    mid_index = 0
    occurrences = []
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        middle_value = numbers[mid_index]

        if middle_value == number_to_find:
            occurrences.append(mid_index)
            break

        if number_to_find < middle_value:
            right_index = mid_index - 1
        else:
            left_index = mid_index + 1
    if len(occurrences) >= 1:
        left = mid_index - 1
        right = mid_index + 1
        while left >= 0 or right < len(numbers):
            if left >= 0:
                if numbers[left] == number_to_find:
                    occurrences.append(left)
                    left -= 1
                else:
                    left = -1
            if right < len(numbers):
                if numbers[right] == number_to_find:
                    occurrences.append(right)
                    right += 1
                else:
                    right = len(numbers)
    print(sorted(occurrences))

if __name__ == "__main__":
    numbers = [1,4,6,9,11,15,15,15,15,17,21,34,34,56,56]
    number_to_find = 15

    find_occurrences(numbers, number_to_find)