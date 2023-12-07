# DLL have one set of pointers going from head to tail and
# one going from tail to head

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def print_list(self):
        temp = self.head
        for _ in range(self.length):
            print(temp.value)
            temp = temp.next

    def append(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            temp.prev = None
            self.tail.next = None
        self.length -= 1
        return temp

    def prepend(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        # works but doing his way, 1 line less of code
        # temp = self.head
        # self.head = node
        # node.next = temp
        # temp.prev = node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.length -= 0
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            # start at tail and go to index
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set(self, value, index):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
        # works but we can use his way and use get to return node or None
        # if index < 0 or index >= self.length:
        #     return None
        # temp = self.head
        # if index < self.length/2:
        #     for _ in range(index):
        #         temp = temp.next
        # else:
        #     temp = self.tail
        #     for _ in range(self.length - 1, index, -1):
        #         # range(start, end at, increment)
        #         temp = self.prev
        # temp.value = value
        # return temp

    def insert(self, value, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            node = Node(value)
            before = self.get(index - 1)
            after = before.next

            # gonna do the 2 sets of before and after arrows
            node.prev = before
            node.next = after
            before.next = node
            after.prev = node
            self.length += 1
            return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        #writing another way (he would use before and after variables) this is just to learn
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
mydll = DoublyLinkedList(6)
mydll.append(1)
mydll.append(2)
mydll.append(3)
# mydll.append(4)
#
# mydll.print_list()
# mydll.pop()
# print()
# mydll.print_list()

print()
mydll.prepend(15)
mydll.print_list()
print()
print(mydll.get(0))
print()
mydll.set(399,2)
mydll.print_list()
print()
mydll.insert(33,2)
mydll.print_list()

name_1 = 'john guy'
name_2 = 'renry guyss'

print(f'{name_1:15}: next')
print(f'{name_2:15}: next')



