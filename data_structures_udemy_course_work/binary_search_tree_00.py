class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        # self.root will be the trees top node or head
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return True

        temp = self.root
        while True:
            if node.value == temp.value:
                return False
            if node.value < temp.value:
                if temp.left is None:
                    temp.left = node
                    return True
                # else
                temp = temp.left

            else:
                if node.value > temp.value:
                    if temp.right is None:
                        temp.right = node
                        return True
                    # else
                    temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            print(f'hi {temp.value}')
            if temp.value == value:
                return True
            # elif temp.left is None or temp.right is None:
            #     return False
            elif temp.value > value:
                temp = temp.left
            else:
                temp = temp.right
        print(f'hi {temp}')
        return False

    def min_value(self):
        # works but we will code one that include subtrees (start anywhere in tree)
        temp = self.root
        while temp.left is not None:
            temp = temp.left
        return temp

    def min_subtree(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

    def dfs_pre_order(self):
        # starts going all the way down left branches of node and then starts one node up from bottom and does right
        # remember call stack and recursion order to understand it
        # starts appending from top down, post will append from bottom to top
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def dfs_post_order(self):
        # will go all the way down leftmost branch until node.left.next = None and right = none, then append that
        # so it appends bottom branch nodes first then upto top branch
        results = []
        

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)
        return results

    def dfs_in_order(self):
        # this is like post order but adds the left most then up one then down right, this leads to min -> max
        # returns lowest to highest number, already sorted
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results

    
me_tree = BinarySearchTree()
me_tree.insert(47)
me_tree.insert(21)
me_tree.insert(76)
me_tree.insert(18)
me_tree.insert(27)
me_tree.insert(52)
me_tree.insert(82)


print(me_tree.root.value)
print(me_tree.root.left.value)
print(me_tree.root.right.value)
print(f'contains {me_tree.contains(5)}')
print(f'min {me_tree.min_value().value}')
print(f'min sub {me_tree.min_subtree(me_tree.root.right).value}')
print('BFS:', me_tree.BFS())
print('traverse pre', me_tree.dfs_pre_order())
print('traverse post', me_tree.dfs_post_order())
print('in order', me_tree.dfs_in_order())
