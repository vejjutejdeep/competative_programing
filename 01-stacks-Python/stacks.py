"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=object):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        if self.head:
            new_element.next = self.head
            self.head = new_element
        else:
            self.head = new_element

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        if self.head:
            current = self.head
            self.head = self.head.next
            current.next = None
            return current
        else:
            return None

    def print_ll(self):
        if self.head:
            current = self.head
            while current.next:
                print(current.value, end=" ")
                current = current.next
            print(current.value)


class stack(object):
    def __init__(self, top=object):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)
        self.ll.print_ll()

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        val = self.ll.delete_first()
        self.ll.print_ll()
        return val
