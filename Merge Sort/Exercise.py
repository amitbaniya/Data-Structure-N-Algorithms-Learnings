


def merge_two_sorted_lists(a,b,elements, key, desc):
    len_a = len(a)
    len_b = len(b)
    i = j =k = 0
    while i < len_a and j < len_b:
        if desc:
            if a[i][key] > b[j][key]:
                elements[k] = a[i]

                i += 1
                k+=1
            else:
                elements[k] = b[j]
                j += 1
                k += 1
        else:
            if a[i][key] < b[j][key]:
                elements[k] = a[i]

                i += 1
                k+=1
            else:
                elements[k] = b[j]
                j += 1
                k += 1

    while i < len_a:
        elements[k] = a[i]
        i+=1
        k += 1

    while j < len_b:
        elements[k] = b[j]
        j+=1
        k += 1



def merge_sort(elements,key, desc = False):
    if len(elements) <= 1:
        return

    mid = len(elements)//2
    left = elements[:mid]
    right = elements[mid:]

    merge_sort(left, key, desc)
    merge_sort(right, key, desc)

    merge_two_sorted_lists(left, right, elements, key, desc)


if __name__ == '__main__':
    elements = [
        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
        {'name': 'rajab', 'age': 12, 'time_hours': 3},
        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
    ]
    arr = [10, 3, 15, 7, 8, 23, 98, 31]
    #print(merge_two_sorted_lists(a,b, arr))
    merge_sort(elements, key='name')
    print(elements)