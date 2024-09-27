class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = LinkedList()

    def enqueue(self, item):
        self.storage.add_to_tail(item)
        self.size += 1

    def dequeue(self):
        freedItem = None
        if self.storage.head != None:
            freedItem = self.storage.head.value
            self.storage.delete_head()
            self.size -= 1
        return freedItem

    def len(self):
        return self.size


class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def set_next(self, node):
        self.next = node

    def get_next(self):
        return self.next

class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_to_head(self, value):
        new_head = Node(value)
        new_head.set_next(self.head)
        if self.head == None:
            self.tail = new_head
        self.head = new_head

    def delete_head(self):
        if self.head == self.tail:
            self.tail = None
            self.head = None
        else:
            self.head = self.head.get_next()

    def add_to_tail(self, value):
        if self.tail == None:
            self.add_to_head(value)
        else:
            new_tail = Node(value)
            self.tail.set_next(new_tail)
            self.tail = new_tail

    def delete_tail(self):
        current = self.head
        while current.get_next() != None:
            current = current.get_next()
        current.set_next(None)
        self.tail = current

    def length(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.get_next()

