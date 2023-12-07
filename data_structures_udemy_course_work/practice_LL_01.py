class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def append(self, value):
        node = Node(value)
        if self.length is None:
            self.head = node
            self.tail = node
        self.tail.next = node
        self.tail = node
        self.length += 1

    def print_all(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def pop(self):
        if self.length == 0:
            self.head = None
            self.tail = None
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        # print(pre.value, temp.value)
        self.tail = pre
        self.tail.next = None
        return temp

    def pop_first(self):
        # print(f'pop first item  length {self.length}')
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            # loop for how many index spots we need to
            # we use _ here bc its used when u don't use it in the loop, i.e. no print(i), just proper syntax
            temp = temp.next
        return temp
        # does work but doing his way
        # count = 0
        # temp = self.head
        # while temp:
        #     if count == index:
        #         return temp
        #     count += 1
        #     temp = temp.next

    def set(self, index, value):
        # create function to give existing node new value when given the nodes index
        # first time calling another method from inside a method
        temp = self.get(index)
        # this either returns None or a node
        if temp is not None:
            temp.value = value
            return True
        return False
        # works but doing his way
        # if index < 0 or index >= self.length:
        #     return None
        # temp = self.head
        # for _ in range(index):
        #     temp = temp.next
        # temp.value = value
        # return temp

    def prepend(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            self.length = 1
        else:
            node.next = self.head
            self.head = node
        self.length += 1
        return True

    def insert(self, index, value):
        # check if index is valid/exists
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            # print('in append')
            return self.append(value)
            # increment to index
        node = Node(value)
        temp = self.head
        pre = self.head
        for _ in range(index):
            pre = temp
            temp = temp.next
        pre.next = node
        node.next = temp
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == (self.length - 1):
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
        #works but not best practice
        # temp = self.head
        # pre = self.head
        # for _ in range(index):
        #     pre = temp
        #     temp = temp.next
        # self.length -= 1
        # pre.next = temp.next
        print(f'pre {prev.value} temp {temp.value}')

    def reverse(self):
        # make sure you know for interview questions, very common
        # starting at tail you need to
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
l3 = LinkedList(1)
l3.append(2)
l3.append(3)
l3.append(4)
l3.print_all()
print()

l3.reverse()

l3.print_all()


# l3.print_all()