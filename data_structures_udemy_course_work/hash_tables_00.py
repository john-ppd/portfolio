class HashTable:
    def __init__(self, size=7):
        # if variable is defined, it is default variable value
        # this is creating a list with size indexes filled with None
        self.data_map = [None] * size

    def __hash(self, key):
        # where we pass key to to determine address to store the key value pair
        my_hash = 0
        for letter in key:
            # ord(letter) gets ascii numerical value of each letter (ordinal)
            # * 23 because it's a prime number, can use any prime number for one way function
            # % makes it so that it gives remainer, since length = 7 this will return 0-6 (our address space)
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            # enumerate returns an object that contains a counter as a key for each value within an object
            print(i, ": ", val)

    def set_item(self, key, value):
        # return index location we're going to use
        index = self.__hash(key)
        # next if value in index is still None we want to create an empty list in the index we got returned
        if self.data_map[index] is None:
            self.data_map[index] = []
        # add our key and value to the empty list
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            # loop through all lists in that index location (we could have multiple since we have finite indexes)
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        # if no value to return, return non (index is empty)
        return None

    def key_list(self):
        all_keys = []
        # since len is a num we use range
        for i in range(len(self.data_map)):
            # if index isnt empty we loop through it
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    # append the key list
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

    def is_match_slow(self, list_0, list_1):
        for i in list_0:
            for j in list_1:
                if i == j:
                    return True
        return False

    def is_match_fast(self, list_0, list_1):
        my_dict = {}
        for i in list_0:
            # create dictionary setting all keys and make values = True
            my_dict[i] = True

        # now we make non nested for loop to keep it On
        for j in list_1:
            # cycle through second list and check for matches
            if j in my_dict:
                return True
        return False
my_hashy = HashTable()

nums_0 = [0, 5, 6, 8, 3]
nums_1 = [10, 15, 16, 18, 3]


# BIG O
# Both Insert and Lookup by key in a Hash Table is O(1) True
# Binary Search Trees are sorted which makes them better at searching for all values that fall within a range.
# since we're going to use many more memory locations it will be rare to have memory shared so its 0(1)
print(f'is match 0n^2: {my_hashy.is_match_slow(nums_0, nums_1)}')
print(f'is match 0n since we 0n to create dictionary, then its 01: {my_hashy.is_match_fast(nums_0, nums_1)}')

my_hashy.set_item('bolts', 500)
my_hashy.set_item('washers', 23)
my_hashy.set_item('lumber', 77)
my_hashy.set_item('sr', 75)

my_hashy.print_table()

print(my_hashy.get_item('lumbers'))
print()
print(my_hashy.key_list())
