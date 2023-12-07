class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    # for stack you only need to keep track of top item, is like tennis balls in tube
    def __init__(self, value):
        node = Node(value)
        self.top = node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print()
    def push(self, value):
        node = Node(value)
        if self.height == 0:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
        self.height -= 1
        return temp
me_stacky = Stack(500)
me_stacky.push(799)
me_stacky.push(4)
me_stacky.push(6)

me_stacky.print_stack()

me_stacky.pop()
me_stacky.print_stack()