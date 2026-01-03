class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)

        return hash % self.MAX

    #add an item to the hashmap as a key value pair
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if element[0] == key and len(element) == 2:
                self.arr[h][index] = (key,value)
                found = True
                break

        if not found:
            self.arr[h].append((key,value))

    #get the item from the hashmap using key
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            print(element[0])
            if element[0] == key:
                print('true')
                return element

        return None

    #to delete the item using key
    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

if __name__ == '__main__':
    ht = HashTable()
    print(ht.get_hash('hello'))

    ht['march 6'] = 180
    ht['march 17'] = 200

    print(ht['march 17'])

    del ht['march 17']

    print(ht.arr)








