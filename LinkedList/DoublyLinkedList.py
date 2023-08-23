class _Node():
    __slots__ = '_element', '_next', '_prev'

    def __init__(self, element, next, prev):
        self._element = element
        self._next = next
        self._prev = prev


class DoublyLinkedList():

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def addfirst(self, element):
        newNode = _Node(element, None, None)
        if self.isempty():
            self._tail = newNode
        else:
            newNode._next = self._head
            self._head._prev = newNode
        self._head = newNode
        self._size += 1

    def addlast(self, element):
        newNode = _Node(element, None, None)
        if self.isempty():
            self._head = newNode
        else:
            newNode._prev = self._tail
            self._tail._next = newNode
        self._tail = newNode
        self._size += 1

    def addany(self, element, position):
        newNode = _Node(element, None, None)
        if self.isempty():
            self._head = newNode
            self._tail = newNode
        else:
            p = self._head
            i = 1
            while i < position - 1:
                p = p._next
                i += 1
            newNode._next = p._next
            newNode._prev = p
            p._next._prev = newNode
            p._next = newNode
        self._size += 1

    def removefirst(self):
        if self.isempty():
            print('List is empty')
            return
        self._head = self._head._next
        self._head._prev = None
        self._size -= 1

    def removelast(self):
        if self.isempty():
            print('List is empty')
            return
        self._tail = self._tail._prev
        self._tail._next = None
        self._size -= 1

    def removeany(self, position):
        if self.isempty():
            print('List is empty')
            return
        p = self._head
        i = 1
        while i <= position - 1:
            p = p._next
            i += 1
        p._next._prev = p._prev
        p._prev._next = p._next
        self._size -= 1

    def display(self):
        p = self._head
        while p:
            print(p._element, end='-->')
            p = p._next
        print()

    def displayrev(self):
        p = self._tail
        while p:
            print(p._element, end='-->')
            p = p._prev
        print()

D = DoublyLinkedList()
D.addlast(7)
D.addlast(4)
D.addlast(12)
D.display()
print('Size:', len(D))
D.displayrev()
D.addlast(8)
D.addlast(3)
D.display()
print('Size:', len(D))
D.displayrev()
D.addany(25, 3)
D.display()
print('Size:', len(D))
D.displayrev()
D.removeany(3)
D.display()
print('Size:', len(D))
D.displayrev()
D.removefirst()
D.display()
print('Size:', len(D))
D.removelast()
D.display()
print('Size:', len(D))