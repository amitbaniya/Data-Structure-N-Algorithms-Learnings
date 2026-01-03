class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)

        return hash % self.MAX

    #add an item to the hashmap as a key value pair
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    #get the item from the hashmap using key
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    #to delete the item using key
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

if __name__ == '__main__':
    ht = HashTable()
    print(ht.get_hash('hello'))

    ht['march 19'] = 180
    ht['march 20'] = 200

    del ht['march 20']
    print(ht['march 20'])







