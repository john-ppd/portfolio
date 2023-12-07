# always write all scenarios out prior to coding
# a node is just a memory location
# pointers will point to it
# they are not in sequential order
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    # the self keyword is to know its a method within a class
    # making a linked list constructor, set head tail and length to 1 starting node

    def __init__(self, value):
        # creates the starting node
        new_node = Node(value)
        self.length = 1
        self.head = new_node
        self.tail = new_node

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True  # not needed but for future lessons we will use

    def pop(self):
        # check first if are no items in LL linked list
        if self.length is None:
            return None

        # make 2 temp variables and point them at head
        temp = self.head
        pre = self.head

        # make a while statement that is true as long as it's pointing at another node
        # way 1 to write:
        # while temp.next is not None:
        # way 2:
        while temp.next:
            # when this loop ends temp will be on last node, pre the node prior to it
            pre = temp
            temp = temp.next
        # now we set tail to where pre is
        self.tail = pre
        # now we remove the last node
        self.tail.next = None
        # make length -= 1
        self.length -= 1
        # in case it is last node we need case for length == 0 here after decrement
        if self.length == 0:
            self.head = None
            self.tail = None

        # return the node that we just removed "temp" in our case
        return temp


new_link = LinkedList(10)
new_link.append(5)
new_link.append(15)
new_link.append(115)
new_link.append(55)

new_link.print_list()
print()
print(f'popped {new_link.pop().value}')

new_link.print_list()
# new_linked_list = LinkedList(4)
# print(new_linked_list.head)
# # prints memory location
# print(new_linked_list.tail)
# print(new_linked_list.head.value)
# new_linked_list.print_list()
