from utils import time_it

@time_it
def bubble_sort(elements, key):
    size = len(elements)

    for j in range(size - 1):
        swapped = False
        for i in range(size - 1 - j):
            if elements[i][key] > elements[i+1][key]:
                temp = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = temp
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    elements = [
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]

    bubble_sort(elements,'device')
    print(elements)