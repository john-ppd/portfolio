class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedListD:
    def __init__(self, value):
        # this is upon creation of LL object, only called the once
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def append(self, value):
        node = Node(value)
        if self.length == 0:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def print_all(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        print()

    def prepend(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def get(self, index):
        if index < 0 or index >= self.length:
            print('bad index')
            return None
        if index <= self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        # print(f'temp: {temp.value}')
        return temp

    def insert(self, value, index):
        if index < 0 or index > self.length:
            return None
        if index == self.length:
            self.append(value)
        else:
            temp = self.get(index)
            temp.value = value

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        temp = self.get(index)
        prev = temp.prev
        post = temp.next
        post.prev = prev
        prev.next = post
        temp.next = None
        temp.prev = None
l3 = LinkedListD(10)
l3.append(15)
l3.append(4)
l3.insert(343,2)
l3.print_all()
l3.remove(1)
l3.print_all()