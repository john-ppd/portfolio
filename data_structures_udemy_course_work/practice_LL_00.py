class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        # initial values
        node = Node(value)
        self.length = 1
        self.head = node
        self.tail = node

    def append(self, value):
        node = Node(value)
        self.tail.next = node
        self.tail = node

    def print_all(self):
        print()
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print()

    def pop(self):
        if self.length is None:
            return None

        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.length -= 1
        # if is now empty, clear pointers
        if self.length is None:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        # add item to beginning of LL
        # check if empty, if so point head and tail to this node
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            self.length = 1
        else:
            node.next = self.head
            self.head = node

            # works but trying to do his way
            # temp = self.head
            # # pre = self
            # self.head = node
            # self.head.next = temp
        self.length += 1
        return True

listss = LinkedList(10)
listss.append(2)
listss.append(9)
listss.append(4)
listss.prepend(1555)
listss.print_all()
print(f'pop:{listss.pop().value}')
listss.print_all()
