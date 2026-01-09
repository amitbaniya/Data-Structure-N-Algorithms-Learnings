class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print_linked_list(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr = llstr + str(itr.data)
            itr = itr.next

        print("Hello",llstr)


if __name__ == '__main__':
    l1 = LinkedList()

    l1.insert_at_beginning(9)
    l1.insert_at_beginning(9)
    l1.insert_at_beginning(9)
    l1.insert_at_beginning(9)
    l1.insert_at_beginning(9)
    l1.insert_at_beginning(9)
    l1.insert_at_beginning(9)

    l1.print_linked_list()

    l2 = LinkedList()
    l2.insert_at_beginning(9)
    l2.insert_at_beginning(9)
    l2.insert_at_beginning(9)
    l2.insert_at_beginning(9)

    l2.print_linked_list()

    llstr = ''
    itr1 = l1.head
    itr2 = l2.head
    carry = 0
    output = None
    individual_sum = 0
    while itr1 or itr2 or carry:
        total = carry
        if itr1:
            total += itr1.data
            itr1 = itr1.next
        if itr2:
            total +=  itr2.data
            itr2 = itr2.next

        num = total % 10
        carry = total // 10

        llstr = str(num) + llstr

    print(llstr)







