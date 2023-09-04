class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next


class LinkedList:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def addlast(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def search(self, key):
        p = self._head
        index = 0
        while p != None:
            if p._element == key:
                return index
            p = p._next
            index += 1

        return -1

    def insertsorted(self, element):
        newNode = _Node(element, None)
        if self.isempty():
            self._head = newNode
        else:
            p = self._head
            q = self._head
            while p and p._element < element:
                q = p
                p = p._next
            if p == self._head:
                newNode._next = self._head
                self._head = newNode
            else:
                newNode._next = q._next
                q._next = newNode
        self._size += 1

    def addfirst(self, element):
        newNode = _Node(element, self._head)
        self._head = newNode
        if self.isempty():
            self._tail = newNode
        self._size += 1

    def addany(self, element, position):
        newNode = _Node(element, None)
        index = 1
        p = self._head

        while index < position - 1:
            p = p._next
            index += 1
        newNode._next = p._next
        p._next = newNode
        self._size += 1

    def removefirst(self):
        if self.isempty():
            print('List is empty')
            return
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.isempty():
            tail = None
        return e

    def removelast(self):
        if self.isempty():
            print('List is empty')
            return
        ele = self._tail._element
        p = self._head
        while p._next != self._tail:
            p = p._next

        p._next = None
        self._tail = p
        self._size -= 1
        return ele

    def removeany(self, position):
        if self.isempty():
            print('List is empty')
            return
        index = 1
        p = self._head

        while index < position - 1:
            p = p._next
            index += 1

        ele = p._next._element
        p._next = p._next._next
        self._size -= 1
        return ele


    def display(self):
        p = self._head
        while p:
            print(p._element, end='-->')
            p = p._next
        print()


# L = LinkedList()
# L.addlast(7)
# L.addlast(4)
# L.addlast(12)
# L.display()
# print('Size', len(L))
# L.addlast(8)
# L.addlast(3)
# L.display()
# print('Size', len(L))
# print('Result', L.search(20))
# L.addfirst(30)
# L.display()
# print('Size', len(L))
# L.addlast(78)
# L.display()
# print('Size', len(L))
# L.addany(101, 2)
# L.display()
# print('Size', len(L))
# ele = L.removefirst()
# print('Element Removed:', ele)
# L.display()
# print('Size', len(L))
# ele = L.removelast()
# print('Element Removed:', ele)
# L.display()
# print('Size', len(L))
# ele = L.removeany(6)
# print('Element Removed:', ele)
# L.display()
# print('Size', len(L))
