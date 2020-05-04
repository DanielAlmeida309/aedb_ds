from tad_list import List
from nodes import SingleListNode
from exceptions import EmptyListException, InvalidPositionException

class SinglyLinkedList(List):
    def __init__(self):
        self.head = None
        self.tail = None
        self.sz = None

    # Returns true iff the list contains no elements.
    def is_empty(self):
        return self.head == None

    # Returns the number of elements in the list.
    def size(self):
        return self.sz

    # Returns the first element of the list.
    # Throws EmptyListException.
    def get_first(self):
        if self.is_empty() == True:
            raise EmptyListException()
        else:
            return self.head

    # Returns the last element of the list.
    # Throws EmptyListException.
    def get_last(self):
        if self.size() == 0:
            raise EmptyListException()
        else:
            return self.tail

    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    def get(self, position):
        node = self.get_first()
        for i in range(self.size()-1):
            if i == position:
                return node.get_element()
            else:
                node = node.get_next()

    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.
    def find(self, element):
        node = self.get_first()
        for i in range(self.size()-1):
            if node.get_element() == element:
                return i
            else:
                node = node.get_next()
        return -1

    # Inserts the specified element at the first position in the list.
    def insert_first(self, element):
        self.sz += 1
        self.head = SingleListNode(element, None)

    # Inserts the specified element at the last position in the list.
    def insert_last(self, element):
        self.sz += 1
        self.tail = SingleListNode(element, None)

    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.
    def insert(self, element, position):
        if element > self.size() and element < 0:
            raise InvalidPositionException()
        else:
            if position == 0:
                old_node = self.get_first()
                nxt_node = old_node.get_next()
                self.insert_first(element)
                new_node = self.get_first()
                new_node.set_next(nxt_node)
                self.sz += 1
            elif position == self.size()-1:
                self.insert_last(element)
                self.sz += 1
            else:
                node = self.get_first()
                for i in range(self.size()-1):
                    node_nxt = node.get_next()
                    if i == position:
                        self.sz += 1
                        new_node = SingleListNode(element,node_nxt)
                        node_bfr.set_next(new_node)
                    else:
                        node_bfr = node
                        node = node_nxt

    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
    def remove_first(self):
        if self.is_empty() == True:
            raise EmptyListException()
        else:
            self.sz -= 1
            node = self.get_first()
            self.insert_first(node.get_next())
            return node.get_element()

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    def remove_last(self):
        if self.size() == 0:
            raise EmptyListException()
        else:
            self.sz -= 1
            node = self.get_last()
            self.tail = None
            return node.get_element()

    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
    def remove(self, position):
        if element > self.size() and element < 0:
            raise InvalidPositionException()
        else:
            node = self.get_first()
            for i in range(self.size()-1):
                node_nxt = node.get_next()
                if i == position:
                    self.sz -= 1
                    node_bfr.set_next(node_nxt)
                    return node.get_element()
                else:
                    node_bfr = node
                    node = node_nxt

    # Removes all elements from the list.
    def make_empty(self):
        self.head = None
        self.tail = None

    # Returns an iterator of the elements in the list (in proper sequence).
    def iterator(self): pass
