class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):
        # base case. Once we reach the end, make that node the head
        if node is None:
            return node
        if node.next_node is None:
            self.head = node
            self.head.next_node = prev
            return
        else:
            self.reverse_list(node.next_node, node)
            node.next_node = prev
            return


"""
       1     <-     2    ->    3    ->   4
prev   node        next        
       prev        node =current
"""

# You need an if statement for when the node is none. You need to set the node's next_node to be prev
# in your second if statement. You're over complicating the else. You should just be able to pass
# in the the node's next node and the node to the params of your recursive function, and then just
# set the next node to the be the prev like you'll have to do for the second if statement.

list = LinkedList()
list.add_to_head(1)
list.add_to_head(2)
list.add_to_head(3)
list.add_to_head(4)
list.add_to_head(5)
# should be 5
print("head:", list.head.value, "should be 5")
list.reverse_list(list.head, None)
# should be 1
print("head:", list.head.value, "should be 1")
