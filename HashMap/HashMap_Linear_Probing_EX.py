class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)

        return hash % self.MAX

    #add an item to the hashmap
    #Check if it already exists and put it in next empty space
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        count = 0
        while self.arr[h] is not None and count < 10 :
            if self.arr[h][0] == key:
                self.arr[h] = (key,value)
                break
            else:
                if h < self.MAX - 1:
                    h += 1
                else:
                    h = 0
            count += 1
        if count == 10 :
            print("No space remaining")

        self.arr[h] = (key,value)



    #get the item from the hashmap using key
    def __getitem__(self, key):
        h = self.get_hash(key)
        count = 0
        while self.arr[h] is not None and count < 10:
            if self.arr[h][0] == key:
                return self.arr[h]
            else:
                if h < self.MAX - 1:
                    h += 1
                else:
                    h = 0
            count += 1
        if count == 10:
            print("Did not find it.")

        return None

    #to delete the item using key
    def __delitem__(self, key):
        h = self.get_hash(key)
        count = 0
        while self.arr[h] is not None and count < 10:
            if self.arr[h][0] == key:
                self.arr[h] = None
                break
            else:
                if h < self.MAX - 1:
                    h += 1
                else:
                    h = 0
            count += 1
        if count == 10:
            print("Did not find it.")

if __name__ == '__main__':
    ht = HashTable()

    ht['march 6'] = 180
    ht['march 17'] = 200
    ht['march 10'] = 200
    ht['march 20'] = 200
    ht['march 30'] = 200
    ht['march 17'] = 200
    ht['march 17'] = 200
    ht['march 17'] = 200
    ht['march 17'] = 200
    ht['march 17'] = 200
    ht['march 30'] = 300

    print(ht['march 17'])

    del ht['march 17']

    print(ht.arr)








