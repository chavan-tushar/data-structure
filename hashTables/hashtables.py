class HashTable:
    def __init__(self, size = 7) -> None:
        self.data_map = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index]:
            self.data_map[index].append([key, value])
        else:
            self.data_map[index] = [[key, value]]

    def get_item(self, key):
        index = self.__hash(key)
        if not self.data_map[index]:
            return None
        elif len(self.data_map[index]) == 1:
            return self.data_map[index][0][1]
        else:
            for item in self.data_map[index][::-1]:
                if item[0] == key:
                    return item[1]
            return None
    
    def keys(self):
        all_keys = []
        for item in self.data_map:
            if not item:
                continue
            elif len(item) == 1:
                all_keys.append(item[0][0])
            else:
                for i in item:
                    all_keys.append(i[0])
        return all_keys


my_hash_table = HashTable()
my_hash_table.print_table()
my_hash_table.set_item("Tushar", 1000)
my_hash_table.set_item("Tushar", 2000)
my_hash_table.set_item("tushar", 2000)
my_hash_table.set_item("Rohini", 2000)
my_hash_table.set_item("Ishna", 2000)
my_hash_table.set_item("Miraya", 2000)
my_hash_table.set_item("Veera", 2000)
my_hash_table.set_item("Aadya", 2000)
my_hash_table.print_table()
print(my_hash_table.get_item("tushar"))
print(my_hash_table.keys())