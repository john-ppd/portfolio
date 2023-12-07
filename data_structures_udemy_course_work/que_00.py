class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        node = Node(value)
        self.first = node
        self.last = node
        self.length = 1

    def enqueue(self, value):
        #enqueue adds to que onto tail of list, pretty well is append
        #having the head be the front of line makes 0(1), tail is 0(n)
        node = Node(value)
        if self.length == 0:
            self.first = node
            self.last = node

        else:
            self.last.next = node
            self.last = node



        self.length += 1


    def print_que(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print()

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp
        # works, doing his tho
        # next_in_que = self.first
        # self.first = next_in_que.next
        # next_in_que.next = None
        # self.length -= 1
        # return next_in_que
qu = Queue(100)
qu.enqueue(200)
qu.enqueue(300)
qu.print_que()
print(f'ququq:{qu.dequeue().value}')
qu.print_que()
print(f'ququq2:{qu.dequeue().value}')
qu.print_que()
print(f'ququq3:{qu.dequeue().value}')
qu.print_que()
