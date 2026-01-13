#-->Lomuto Partition
'''------> Here you first choose the pivot point which we choose last one, then 
            we start with p-index which is the start of the list, then iterate
            this p-index until it finds the value greater than pivot point, 
            then when it finds it, stop the pivot point and search from there 
            a item that is less than pivot point. then when you find it swap it with
            p-index and do the repeatedly. And at the end you will see that the pivot point 
            is in the right position in an array or is sorted.'''

def partition_recursive(elements, p_index, pivot_index):
    pivot_point = elements[pivot_index]
    i = p_index

    while i < pivot_index:
        while elements[p_index] <= pivot_point and p_index < pivot_index:
            p_index += 1
        i = p_index
        while elements[i] > pivot_point and p_index < len(elements):
            i += 1

        elements[p_index], elements[i] = elements[i], elements[p_index]


    return p_index

def quick_sort(elements, p_index, pivot_index):
    if p_index < pivot_index:
        pi = partition_recursive(elements,p_index, pivot_index)
        quick_sort(elements, p_index, pi-1)
        quick_sort(elements, pi+1, len(elements) - 1)


if __name__ == "__main__":
    elements = [11, 9, 29, 7, 2, 15, 28]
    tests = [
        [11,11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]
    quick_sort(elements,0, len(elements) - 1)
    for each in tests:
        quick_sort(each, 0, len(each) - 1)
        print(each)
    print(elements)
