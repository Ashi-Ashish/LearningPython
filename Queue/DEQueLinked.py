class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next


class DEQueLinked:

    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def addlast(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._front = newest
        else:
            self._rear._next = newest
        self._rear = newest
        self._size += 1

    def addfirst(self, element):
        newNode = _Node(element, self._front)
        self._front = newNode
        if self.isempty():
            self._rear = newNode
        self._size += 1

    def search(self, key):
        p = self._front
        index = 0
        while p != None:
            if p._element == key:
                return index
            p = p._next
            index += 1

        return -1

    def removefirst(self):
        if self.isempty():
            print('List is empty')
            return
        e = self._front._element
        self._front = self._front._next
        self._size -= 1
        if self.isempty():
            tail = None
        return e

    def removelast(self):
        if self.isempty():
            print('List is empty')
            return
        ele = self._rear._element
        p = self._front
        while p._next != self._rear:
            p = p._next

        p._next = None
        self._rear = p
        self._size -= 1
        return ele

    def first(self):
        if self.isempty():
            print('DEQue is Empty')
            return
        return self._front._element

    def last(self):
        if self.isempty():
            print('DEQue is Empty')
            return
        return self._rear._element

    def display(self):
        p = self._front
        while p:
            print(p._element, end='-->')
            p = p._next
        print()


D = DEQueLinked()
D.addfirst(5)
D.addfirst(3)
D.addlast(7)
D.addlast(12)
D.display()
print('Length:', len(D))
print('Element Removed:', D.removefirst())
print('Element Removed:', D.removelast())
D.display()
print('First Element:', D.first())
print('Last Element:', D.last())
print('Length', len(D))
