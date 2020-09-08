
class Node:
    def __init__(self, value, next_node = None):
        # the value that the node is holding
        self.value = value
        # reference to the next node in the linked list
        self.next_node = None   
# when constructing a new node the next will be "none"

    # method to get the value of the node
    def get_value(self):
        return self.value

    # method to get the node's `next_node`
    def get_next(self):
        return self.next_node

    # method to updat the node's `next_node to the input`
    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


# To add TAIL we have to start from the HEAD 
# and work our way to the end of the linked list 
# to add a new element

    def add_to_tail(self, value):
        #1. create a new node from the value
        # wrap value in a Node
        new_node = Node(value)
        # check to see if the linked list is empty
        if self.head is None and self.tail is None:
        # set head &  tail to the new_node
            self.head = new_node
            self.tail = new_node
        else:
        #2. set the old tail to point to the new node
            self.tail.set_next(new_node)
        #3. reassign tail to refer to the new node
            self.tail = new_node
    
    def remove_head(self):
        # is my linked list empty?
        if self.head is None and self.tail is None:
            return None
        #both head and tail are pointing to the same node
        if self.head == self.tail:
            val = self.head.get_value()
            # delete the linked list's head reference 
            self.head = None
            # delete the linked list's tail reference
            self.tail = None
            return val
        else: 
        # set old head's value that we need to return 
            val = self.head.get_value()
        #set self.head to the old head's next_node
            self.head = self.head.get_next()
        # return the old head's vaule
            return val


    def remove_tail(self):
        # if linked list is empty
        if self.head is None and self.tail is None:
            return None
        # if we have a non-empty linked list
        # move self.tail to previous node
        # start at the HEAD -->
        # itereate over linked list

        if self.head == self.tail: 
        #store the node we're removing value
        # set tail & head to NONE
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val

        # if linked list has more than one Node
        # store the last Node's value in another variable to return it
        else: 
            val = self.tail.get_value()
        #set self.tail to the second to last node
        current = self.head
        # keep iterating until the node after `current` is the tail
        while current.get_next() != self.tail:
            # keep iterating
            current = current.get_next()

        # set self.tail to `current`
        self.tail = current
        # set the new tail's `next_node` to NONE
        self.tail.set_next(None)
        return val

# ll = Node(1)
# ll.set_next = (Node(2))
# ll.next.set_next = Node(3)
# ll.next.next.set_next = Node(4)
# ll.next.next.next.set_next = Node(5)



