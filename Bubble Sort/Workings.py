from utils import time_it

@time_it
def bubble_sort(elements):
    size = len(elements)

    for j in range(size - 1):
        swapped = False
        for i in range(size - 1 - j):
            if elements[i] > elements[i+1]:
                temp = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = temp
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    elements = [5, 9, 2, 1, 67, 34, 88, 34]

    bubble_sort(elements)
    print(elements)