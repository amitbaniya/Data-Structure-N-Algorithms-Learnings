def running_median(elements):

    for i in range(1, len(elements)):
        running_index = i
        print(find_median(elements[0:running_index]))
        anchor = elements[i]
        j = i -1
        while j >=0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j = j -1
        elements[j+1] = anchor
    print(find_median(elements[0:len(elements)]))

def find_median(elements):
    if len(elements) == 1:
        return elements[0]
    elif len(elements) % 2 == 0:
        second_element_index = int(len(elements)/ 2)
        first_element_index = second_element_index - 1
        return (elements[first_element_index] + elements[second_element_index])/2
    else:
        return elements[int(((len(elements) + 1)/ 2) - 1)]


if __name__ == '__main__':
    elements = [2, 1, 5, 7, 2, 0, 5]
    running_median(elements)
