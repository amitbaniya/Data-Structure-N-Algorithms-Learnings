#Two Types of Partitions(Basically a way to put pivot point)
#-->Hoare Partition
'''----> You first choose the pivot point ,
        Then you put start pooint and end point, you first iterate start point
        and iterate it until it finds greater than the pivot point
        Then you iterate from the end until you find less than the pivot point.
        and once you find both greater and less than the pivot point, you swap the
        greater and less than element with each other. Then you continue doing the
        same process until you cross the end point with start point.
        After you cross, you swap the end point with pivot point.
        This will set the pivot point/item in its right position in an array'''
#-->Lomuto Partition
'''------> Here you first choose the pivot point which we choose last one, then 
            we start with p-index which is the start of the list, then iterate
            this p-index until it finds the value greater than pivot point, 
            then when it finds it, stop the pivot point and search from there 
            a item that is less than pivot point. then when you find it swap it with
            p-index and do the repeatedly. And at the end you will see that the pivot point 
            is in the right position in an array or is sorted.'''

def partition(elements):
    pivot_point = elements[0]
    start_point = 1
    end_point = len(elements) - 1

    while True:

        if elements[start_point] < pivot_point:
            start_point += 1
        if elements[end_point] > pivot_point:
            end_point -= 1
        if elements[start_point] > pivot_point > elements[end_point] and start_point < end_point:
            print(elements)
            elements[start_point], elements[end_point] = elements[end_point], elements[start_point]

        if end_point < start_point :
            elements[0],elements[end_point] = elements[end_point],elements[0]
            break

    print(elements)

def partition_recursive(elements, start_point, end_point):
    pivot_index = start_point
    pivot_point = elements[pivot_index]
    while start_point < end_point:
        while elements[start_point] <= pivot_point and start_point < end_point:
            start_point += 1

        while elements[end_point] > pivot_point :
            end_point -= 1
        if  start_point < end_point:
            elements[start_point], elements[end_point] = elements[end_point], elements[start_point]

    elements[pivot_index], elements[end_point] = elements[end_point], elements[pivot_index]


    return end_point

def quick_sort(elements, start, end):
    if start < end:
        pi = partition_recursive(elements,start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, len(elements) - 1)


if __name__ == "__main__":
    elements = [11, 9, 29, 7, 2, 15, 28]
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
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
